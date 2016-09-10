This is a fork of http://www.vim.org/scripts/script.php?script_id=2473

The python_open_module.vim is the script that allows you open the module file
below the cursor when coding python. It's easy to use. For example, you can
create a new python file and input:

    import os

move the cursor above `os` and press `<LocalLeader>oo` (`\oo` in common
in vim) in normal mode and you will see the argparse.py file opened in the
current window.  You can continue to type

    os.walk

now hit the same keys and you can see os.py file opened and the cursor at
the `walk` function.

The open fails if the module is builtin such as `sys` or is not available.

There are three options for mapping keys which you can change to any other key:

    let g:pom_key_open='<LocalLeader>oo'         # open module file in the current window
    let g:pom_key_open_in_win='<LocalLeader>ow'  # open module file in a new window
    let g:pom_key_open_in_tab='<LocalLeader>ot'  # open module file in a tab

Requires vim compiled with +python or +python3.  If you have both, you can
ask for either with

    let g:pom_python='python'  # or 'python3'

Changes in my fork:

- support +python3
- rewritten README to be in Markdown
- some bugfixes
