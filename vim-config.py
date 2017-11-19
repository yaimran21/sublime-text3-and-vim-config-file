   "Sample .vimrc file by Md Imran hossain
   "
   " " ============================================
   " " Note to myself:
   " " DO NOT USE <C-z> FOR SAVING WHEN PRESENTING!
   " " ============================================
  
    "For Background color
    set background=dark
  
   "Resposible for all plugin
  call plug#begin('~/.vim/plugged')
       Plug 'scrooloose/nerdtree'
       Plug 'flazz/vim-colorschemes'
       Plug 'nrocco/vim-phplint'
       Plug 'scrooloose/syntastic'
       Plug 'klen/python-mode'
 call plug#end()
  
 20 "For NERDTreeToggle
 21  map <C-n> :NERDTreeToggle<CR>
 22 
 23 "For color themes
 24  colorscheme PaperColor
 25 
 26 ""For all status
 27 set statusline+=%#warningmsg#
 28 set statusline+=%{SyntasticStatuslineFlag()}
 29 set statusline+=%*
 30 set statusline+=%#warningmsg#
 31 set statusline+=%{SyntasticStatuslineFlag()}
 32 set statusline+=%*
 33 
 34 ""For python3. version specify
 35 let g:pymode_python = 'python3'
 36 let g:syntastic_python_python_exec = "/usr/local/bin/python3"
 37 
 38 
 39 " " Automatic reloading of .vimrc
 40 " "" autocmd! bufwritepost .vimrc source %
 41 "
" " Better copy & paste
 44 " " When you want to paste large blocks of code into vim, press F2 before you
 45 " " paste. At the bottom you should see ``-- INSERT (paste) --``.
 46 "
 47 "" set pastetoggle=<F2>
 48 "" set clipboard=unnamed"
 49 "
 50 " " Mouse and backspace
 51 ""set mouse=a  " on OSX press ALT and click
 52 ""set bs=2     " make backspace behave like normal again
 53 
 54 " " Rebind <Leader> key
 55 " " I like to have it here becuase it is easier to reach than the default and
 56 " " it is next to ``m`` and ``n`` which I use for navigating between tabs.
 57 " "" let mapleader = ","
 58 "
 59 "
 60 " " Bind nohl
 61 " " Removes highlight of your last search
 62 " " ``<C>`` stands for ``CTRL`` and therefore ``<C-n>`` stands for ``CTRL+n``
 63 " "" noremap <C-n> :nohl<CR>
 64 " "" vnoremap <C-n> :nohl<CR>
 65 " "" inoremap <C-n> :nohl<CR>
 66 "
 67 "
 68 " " Quicksave command
 69 " "" noremap <C-Z> :update<CR>
 70 " "" vnoremap <C-Z> <C-C>:update<CR>
 71 " "" inoremap <C-Z> <C-O>:update<CR>
 72 "
 73 "
 74 " Quick quit command
 75 ""noremap <Leader>e :quit<CR>  " Quit current window
 76 ""noremap <Leader>E :qa!<CR>   " Quit all windows
 77 "
 78 "
 79 " " bind Ctrl+<movement> keys to move around the windows, instead of using
 80 " Ctrl+w + <movement>
 81 " " Every unnecessary keystroke that can be saved is good for your health :)
" "" map <c-j> <c-w>j
 83 " "" map <c-k> <c-w>k
 84 " "" map <c-l> <c-w>l
 85 " "" map <c-h> <c-w>h
 86 "
 87 "
 88 " " easier moving between tabs
 89 " "" map <Leader>n <esc>:tabprevious<CR>
 90 " "" map <Leader>m <esc>:tabnext<CR>
 91 "
 92 "
 93 " " map sort function to a key
 94 " "" vnoremap <Leader>s :sort<CR>
 95 "
 96 "
 97 " " easier moving of code blocks
 98 " " Try to go into visual mode (v), thenselect several lines of code here and
 99 " " then press ``>`` several times.
100 " "" vnoremap < <gv  " better indentation
101 " "" vnoremap > >gv  " better indentation
102 "
103 "
104 " " Show whitespace
105 " " MUST be inserted BEFORE the colorscheme command
106 ""autocmd ColorScheme * highlight ExtraWhitespace ctermbg=red guibg=red
107 ""au InsertLeave * match ExtraWhitespace /\s\+$/
108 "
109 "
110 " " Color scheme
111 " " mkdir -p ~/.vim/colors && cd ~/.vim/colors
112 " " wget -O wombat256mod.vim
113 " http://www.vim.org/scripts/download_script.php?src_id=13400
114 set t_Co=256
115 ""color wombat256mod
116 "
117 "
118 " " Enable syntax highlighting
119 " " You need to reload this file for the change to apply
120 filetype off
121 filetype plugin indent on
syntax on
123 "
124 "
125 " " Showing line numbers and length
126 set number  " show line numbers
127 ""set tw=79   " width of document (used by gd)
128 "
129 ""
130 set nowrap  " don't automatically wrap on load
131 ""set fo-=t   " don't automatically wrap text when typing
132 ""set colorcolumn=80
133 highlight ColorColumn ctermbg=233
134 "
135 "
136 " " easier formatting of paragraphs
137 ""vmap Q gq
138 ""nmap Q gqap
139 "
140 "
141 " " Useful settings
142 set history=700
143 set undolevels=700
144 "
145 "
146 " " Real programmers don't use TABs but spaces
147 set tabstop=4
148 set softtabstop=4
149 set shiftwidth=4
150 set shiftround
151 set expandtab
152 "
153 "
154 " " Make search case insensitive
155 set hlsearch
156 set incsearch
157 set ignorecase
158 set smartcase
159 "
160 "
161 " " Disable stupid backup and swap files - they trigger too many events
" " for file system watchers
163 set nobackup
164 set nowritebackup
165 set noswapfile
166 "
167 "
168 " " Setup Pathogen to manage your plugins
169 " " mkdir -p ~/.vim/autoload ~/.vim/bundle
170 " " curl -so ~/.vim/autoload/pathogen.vim
171 " https://raw.githubusercontent.com/tpope/vim-pathogen/master/autoload/pathogen.vim
172 " " Now you can install any plugin into a .vim/bundle/plugin-name/ folder
173 ""call pathogen#infect()
174 "
175 "
176 " "
177 " ============================================================================
178 " " Python IDE Setup
179 " "
180 " ============================================================================
181 "
182 " " Settings for vim-powerline
183 " " cd ~/.vim/bundle
184 " " git clone git://github.com/Lokaltog/vim-powerline.git
185 " "" set laststatus=2
186 "
187 "
188 " " Settings for ctrlp
189 " " cd ~/.vim/bundle
190 " " git clone https://github.com/kien/ctrlp.vim.git
191 " "" let g:ctrlp_max_height = 30
192 " "" set wildignore+=*.pyc
193 " "" set wildignore+=*_build/*
194 " "" set wildignore+=*/coverage/*
195 "
196 "
197 " " Settings for python-mode
198 " " Note: I'm no longer using this. Leave this commented out
199 " " and uncomment the part about jedi-vim instead
200 " " cd ~/.vim/bundle
" " git clone https://github.com/klen/python-mode
202 " "" map <Leader>g :call RopeGotoDefinition()<CR>
203 " "" let ropevim_enable_shortcuts = 1
204 " "" let g:pymode_rope_goto_def_newwin = "vnew"
205 " "" let g:pymode_rope_extended_complete = 1
206 " "" let g:pymode_breakpoint = 0
207 " "" let g:pymode_syntax = 1
208 " "" let g:pymode_syntax_builtin_objs = 0
209 " "" let g:pymode_syntax_builtin_funcs = 0
210 " "" map <Leader>b Oimport ipdb; ipdb.set_trace() # BREAKPOINT<C-c>
211 "
212 " " Settings for jedi-vim
213 " " cd ~/.vim/bundle
214 " " git clone git://github.com/davidhalter/jedi-vim.git
215 " "" let g:jedi#usages_command = "<leader>z"
216 " "" let g:jedi#popup_on_dot = 0
217 " "" let g:jedi#popup_select_first = 0
218 " "" map <Leader>b Oimport ipdb; ipdb.set_trace() # BREAKPOINT<C-c>
219 "
220 " " Better navigating through omnicomplete option list
221 " " See
222 " http://stackoverflow.com/questions/2170023/how-to-map-keys-for-popup-menu-in-vim
223 " "" set completeopt=longest,menuone
224 " "" function! OmniPopup(action)
225 " ""     if pumvisible()
226 " ""         if a:action == 'j'
227 " ""             return "\<C-N>"
228 " ""         elseif a:action == 'k'
229 " ""             return "\<C-P>"
230 " ""         endif
231 " ""     endif
232 " ""     return a:action
233 " "" endfunction
234 "
235 " "" inoremap <silent><C-j> <C-R>=OmniPopup('j')<CR>
236 " "" inoremap <silent><C-k> <C-R>=OmniPopup('k')<CR>
237 "
238 "
239 " " Python folding
240 " " mkdir -p ~/.vim/ftplugin
241 " " wget -O ~/.vim/ftplugin/python_editing.vim
242 " http://www.vim.org/scripts/download_script.php?src_id=5492
243 " "" set nofoldenable
