# Suppresses fish's intro message
set fish_greeting
#init starship prompt 
starship init fish | source

alias ls="exa -l --icons --group-directories-first"
alias la="exa -la --icons --group-directories-first"
alias emacs="emacsclient -c -a 'emacs' "
alias doom="~/.config/emacs/bin/doom"
