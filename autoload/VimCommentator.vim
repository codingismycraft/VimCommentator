let g:plugin_path = expand('<sfile>:p:h')
let g:path_was_added = 0

function! VimCommentator#ToggleComments()
" Toggles comments on the selected lines.

python3 << endpython
import os
import sys
import vim

was_added = int(vim.eval("g:path_was_added"))

if not was_added:
    path = vim.eval("g:plugin_path")
    path = os.path.dirname(path)
    print("inserting path: ", path)
    sys.path.insert(0, path)
    vim.command("let g:path_was_added = 1")

import vim_commentator.commentator as commentator

l1 = int(vim.eval("""line("'<")""")) 
l2 = int(vim.eval("""line("'>")"""))

lines = [vim.eval(f"getline({line})") for line in range(l1, l2 + 1)]

lines = commentator.toggleComments(lines, '#')


#iElines = [ "ac " + l   for l in lines] 

for index, txt in enumerate(lines):
    txt = txt.replace('"', '\\"')
    cmd = f'call setline({index+l1}, "{txt}")'
    vim.command(cmd) 


endpython
endfunction
