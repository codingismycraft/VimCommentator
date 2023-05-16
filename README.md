# VimCommentator
VimCommentator is a vim plugin that allows for commenting and uncommenting lines of
code using visual selections and the <C-/> (Control and forward slash)
keyboard combination.


## Installation
The preferred method of installation is using Vundle. However, other plugin
installers should work fine as well (although they have not been tested). To
install using Vundle, add the following lines to your .vimrc file:

```
call vundle#begin()
Plugin 'gmarik/Vundle.vim'
Plugin 'codingismycraft/VimCommentator'
call vundle#end()
```

## Usage
To toggle the comment status for a chunk of code, follow these steps:

- Select the code you want to comment using the visual mode.
- Press Control + / to toggle the comment status.

That's it! The selected code will be commented or uncommented accordingly.

Note: The <C-/> keyboard combination may vary depending on your keyboard layout
or operating system configuration.

