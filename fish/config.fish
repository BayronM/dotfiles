# Suppresses fish's intro message
set fish_greeting
#init starship prompt 
starship init fish | source

alias ls="exa -l --icons --group-directories-first"
alias la="exa -la --icons --group-directories-first"
alias emacs="emacsclient -c -a 'emacs' "
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
if test -f /home/bayron/anaconda3/bin/conda
    eval /home/bayron/anaconda3/bin/conda "shell.fish" "hook" $argv | source
end
# <<< conda initialize <<<

scheme set default
