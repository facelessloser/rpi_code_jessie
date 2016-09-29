syntax on
set number
autocmd FileType python set tabstop=4|set shiftwidth=4|set expandtab |set autoindent|set clipboard=unnamed

"autocmd FileType make set tabstop=4|set shiftwidth=4|set expandtab |set autoindent|set clipboard=unnamed
autocmd FileType make set clipboard=unnamed

autocmd FileType c set tabstop=2|set shiftwidth=2|set expandtab |set autoindent|set clipboard=unnamed

au BufNewFile,BufRead *.ino set filetype=c

autocmd FileType lua set tabstop=2|set shiftwidth=2|set expandtab |set autoindent|set clipboard=unnamed

autocmd FileType txt set tabstop=2|set shiftwidth=2|set expandtab |set autoindent|set clipboard=unnamed
