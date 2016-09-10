if !exists("g:pom_python")
    if has("python3")
        let g:pom_python = "python3"
    else
        let g:pom_python = "python"
    endif
endif

execute g:pom_python 'import python_open_module'

function python_open_module#open()
    execute g:pom_python 'python_open_module.pm.open()'
endfunction

function python_open_module#open_in_win()
    execute g:pom_python 'python_open_module.pm.open_in_win()'
endfunction

function python_open_module#open_in_tab()
    execute g:pom_python 'python_open_module.pm.open_in_tab()'
endfunction
