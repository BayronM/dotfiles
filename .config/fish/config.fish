# Suppresses fish's intro message
set fish_greeting
#init starship prompt 
starship init fish | source

alias ls="exa -l --icons --group-directories-first"
alias la="exa -la --icons --group-directories-first"
alias emacs="emacsclient -c -a 'emacs' "
alias doom="~/.config/emacs/bin/doom"
alias ssd="cd /mnt/ssd"
alias hdd="cd /mnt/hdd"
alias cat="bat"

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
if test -f /home/bayron/miniconda3/bin/conda
    eval /home/bayron/miniconda3/bin/conda "shell.fish" "hook" $argv | source
else
    if test -f "/home/bayron/miniconda3/etc/fish/conf.d/conda.fish"
        . "/home/bayron/miniconda3/etc/fish/conf.d/conda.fish"
    else
        set -x PATH "/home/bayron/miniconda3/bin" $PATH
    end
end
# <<< conda initialize <<<

