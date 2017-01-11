"""
" HACK to fore-reload it from vim with :source %
execute g:pom_python 'import sys; sys.modules.pop("python_open_module", None); import python_open_module'
finish
"""
import vim
import inspect
import ast
from types import FunctionType, ModuleType, MethodType

try:
    from types import ClassType
except ImportError:
    # Python 3
    ClassType = None


class ImportVisitor(ast.NodeVisitor):
    def __init__(self):
        self.imports = {}

    def visit_ImportFrom(self, node):
        for alias in node.names:
            _name = alias.asname or alias.name
            self.imports[_name] = "%s.%s" % (node.module, alias.name)

    def visit_Import(self, node):
        for alias in node.names:
            _name = alias.asname or alias.name
            self.imports[_name] = alias.name

class PyModuleOpener(object):
    def __init__(self):
        self.visitor = ImportVisitor()

    def get_imports(self):
        source = vim.current.buffer[:]
        for line in source:
            # XXX: ignores multi-line imports instead of handling them
            if line.strip().startswith(('import ', 'from ')):
                try:
                    tree = ast.parse(line.lstrip())
                except SyntaxError:
                    pass
                else:
                    self.visitor.visit(tree)
        return self.visitor.imports

    def get_real_mod(self, modname):
        imports = self.get_imports()
        if imports:
            for _mod, _real in imports.items():
                if modname == _mod or modname.startswith(_mod + '.'):
                    real_mod = _real + modname.partition(_mod)[-1]
                    return real_mod

    def importmod(self, modname):
        if not modname:
            raise ImportError
        modlist = modname.split('.')
        _modname = modlist[0]
        mod = __import__(_modname, {})
        if len(modlist) > 1:
            for m in modlist[1:]:
                if hasattr(mod, m):
                    _mod = getattr(mod, m)
                    if type(_mod) in (FunctionType, type, ClassType, ModuleType, MethodType):
                        mod = _mod
                    else:
                        break
                else:
                    break
        return mod

    def locate(self, mod):
        fname = inspect.getsourcefile(mod)
        _, linenum = inspect.getsourcelines(mod)
        return fname, linenum

    def open(self):
        fname, linenum = self._open()
        if fname:
            cmd = 'hide edit %s | %d' % (fname, linenum+1)
            vim.command(cmd)

    def open_in_win(self):
        fname, linenum = self._open()
        if fname:
            cmd = 'new %s | %d' % (fname, linenum+1)
            vim.command(cmd)

    def open_in_tab(self):
        fname, linenum = self._open()
        if fname:
            cmd = 'tabnew %s | %d' % (fname, linenum+1)
            vim.command(cmd)

    def _open(self):
        try:
            modname = vim.eval("expand('<cfile>')")
            real_mod = self.get_real_mod(modname)
            mod = self.importmod(real_mod)
            fname, linenum = self.locate(mod)
            return fname, linenum
        except TypeError:
            msg = 'Cannot open source because it is a builtin module.'
            vim.command('echohl ErrorMsg | echomsg "%s" | echohl None' % msg)
            return None, None
        except Exception:
            raise
            msg = 'Cannot open source, maybe it is not a valid module, class or function.'
            vim.command('echohl ErrorMsg | echomsg "%s" | echohl None' % msg)
            return None, None


pm = PyModuleOpener()
