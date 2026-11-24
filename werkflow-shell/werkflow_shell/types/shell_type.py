from enum import Enum


class ShellType(Enum):
    ZSH = 'zsh'
    BASH = 'bash'
    SH = 'sh'
    ASH = 'ash'
    DASH = 'dash'
    FISH = 'fish'
    POWERSHELL = 'powershell'
    PWSH = 'pwsh'
    CMD = 'cmd'
