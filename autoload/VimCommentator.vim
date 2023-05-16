" Vim Commentator 

" This script defines a function that toggles comments on the selected lines.
" It uses the Python 3 integration in Vim to execute the necessary operations.

" Usage:
" 1. Select the lines you want to toggle comments on.
" 2. Call the function `VimCommentator#ToggleComments()`.

" Variables:
" - `s:plugin_path`: Stores the path of the current plugin file.
" - `s:path_was_added`: Flag to indicate if the plugin path was added to the Python system path.

" Dependencies:
" - The Python module `vim_commentator.commentator` is required for comment toggling.


let s:plugin_path = expand('<sfile>:p:h')
let s:path_was_added = 0

function! VimCommentator#ToggleComments()
" Toggles comments on the selected lines.

python3 << endpython
import os
import sys
import vim

file_type = vim.eval("&filetype").strip()

comment_out_char = None

if file_type == 'python':
    comment_out_char = '#'
elif file_type == 'cpp':
    comment_out_char = '//'
elif file_type == 'c':
    comment_out_char = '//'
elif file_type == 'sh':
    comment_out_char = '#'
elif file_type == 'vim':
    comment_out_char = '"'
elif file_type == 'make':
    comment_out_char = '#'
elif file_type == 'javascript':
    comment_out_char = '//'
else:
    print("File type is not supported..")
    
if comment_out_char:
    # Trick to make the vim_commentator package available,
    was_added = int(vim.eval("s:path_was_added"))
    if not was_added:
        path = vim.eval("s:plugin_path")
        path = os.path.dirname(path)
        sys.path.insert(0, path)
        vim.command("let s:path_was_added = 1")

    import vim_commentator.commentator as commentator

    # Get the selection line indexes.
    l1 = int(vim.eval("""line("'<")""")) 
    l2 = int(vim.eval("""line("'>")"""))

    # Load the selected lines in a list.
    lines = [vim.eval(f"getline({line})") for line in range(l1, l2 + 1)]

    # Toggle the comment status for the selection.
    lines = commentator.toggleComments(lines, comment_out_char)

    # Substiture the selected lines with the toggled ones.
    for index, txt in enumerate(lines):
        txt = txt.replace('"', '\\"')
        cmd = f'call setline({index+l1}, "{txt}")'
        vim.command(cmd) 
endpython
endfunction
