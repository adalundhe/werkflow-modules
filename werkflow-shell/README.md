# werkflow-shell

Version `0.2.0`

Cross-platform asynchronous shell execution, environment management, and filesystem operations module for [Werkflow](https://github.com/adalundhe/werkflow).

## Installation

```bash
pip install werkflow-shell
```

## Supported Platforms & Shells

`ShellResolver` automatically selects the right shell implementation based on OS, Linux distribution, `$SHELL`, and installed binaries, or you can override explicitly via `Shell(shell_type=ShellType.<TYPE>)`:

- **macOS:** `ZSHShell` (`zsh`), `BashShell` (`bash`), `FishShell` (`fish`), `ShShell` (`sh`)
- **Linux (Debian/Ubuntu, RHEL/Fedora/Rocky/Alma, Amazon Linux, Arch/Manjaro/CachyOS, Alpine, openSUSE, Gentoo, Void, NixOS, Slackware):** `BashShell`, `ZSHShell`, `FishShell`, `ShShell` (`ash`/`dash`/`sh`)
- **Windows:** `PowerShellShell` (`pwsh` / `powershell.exe`) and `CmdShell` (`cmd.exe`)

## Features

- **Safe Argument Parsing:** `run()` uses `shlex.split` (preserving quoted arguments with spaces) for direct execution and explicit shell invocation (`-c` / `-Command` / `/c`) when `as_shell=True`.
- **Environment Sync:** `get_envar()`, `set_envar()`, `source()`, `eval()`, and `append_to_envfile()` keep `shell.env` and `os.environ` synchronized, capturing environment changes from sourced scripts and `eval` subshells across POSIX, Fish, PowerShell, and CMD.
- **Privilege Escalation:** `assume_admin()` supports `sudo`, `doas`, and `su` on POSIX, and administrator elevation checks on Windows.
- **Async Filesystem Utilities:** `which()`, `get_current_directory()`, `change_directory()`, `to_absolute_path()`, `to_relative_path()`, `create_directory()`, `create_file()`, `touch()`, `copy()`, `move()`, `rm()`, `pipe_to_file()`, `read_file()`, `read_file_as_bytes()`, `check_path_exists()`, `check_if_is_file()`, `check_if_is_directory()`, and `check_file_access()`.
- **Async Lifecycle:** Supports `async with Shell() as shell:`, `await shell.close()`, and `shell.abort()`.

## Usage

```python
from werkflow_shell import Shell, ShellType

async with Shell() as shell:
    result = await shell.run('echo "hello world"', silent=True)
    print(result.stdout.strip())

    await shell.set_envar("APP_ENV", "production")
    await shell.source("./env.sh", silent=True)
    cwd = await shell.get_current_directory()
```

## Dependencies

- `werkflow-core`
- `werkflow-system`

## Requirements

- Python `>=3.11`
