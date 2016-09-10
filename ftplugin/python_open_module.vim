" Original author: tocer tocer.deng@gmail.com
" Maintainer: Marius Gedminas <marius@gedmin.as>
" Version: 1.1.0mg

if !exists("g:pom_key_open")
    let g:pom_key_open = '<LocalLeader>oo'
endif
if !exists("g:pom_key_open_in_win")
    let g:pom_key_open_in_win = '<LocalLeader>ow'
endif
if !exists("g:pom_key_open_in_tab")
    let g:pom_key_open_in_tab = '<LocalLeader>ot'
endif

execute 'noremap <buffer> ' . g:pom_key_open . ' :call python_open_module#open()<CR>'
execute 'noremap <buffer> ' . g:pom_key_open_in_win . ' :call python_open_module#open_in_win()<CR>'
execute 'noremap <buffer> ' . g:pom_key_open_in_tab . ' :call python_open_module#open_in_tab()<CR>'
