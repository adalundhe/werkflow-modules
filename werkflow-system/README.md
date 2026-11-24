# werkflow-system

Version `0.4.0`

Cross-platform operating system, Linux distribution, CPU, memory, drive, architecture, and user inspection module for [Werkflow](https://github.com/adalundhe/werkflow).

## Installation

```bash
pip install werkflow-system
```

## Features

- **Operating System Detection (`System.os`):**
  - **macOS** (`MacOS`): version detection and Apple Silicon / x86_64 architecture support.
  - **Linux** (`Linux`): full distribution detection via `distro` (`id`, `name`, `version`, `codename`, `like`, `package_manager`) and `LinuxDistroFamily` classification (`DEBIAN`, `REDHAT`, `AMAZON`, `ARCH`, `ALPINE`, `SUSE`, `GENTOO`, `VOID`, `NIXOS`, `SLACKWARE`, `GENERIC`), supporting `x86_64`, `aarch64`/`arm64`, `armv7l`, `i686`, `ppc64le`, `s390x`, and `riscv64`.
  - **Windows** (`Windows`): Windows 10/11 build-number detection and `x86_64`/`AMD64`/`ARM64` support.
- **Hardware & Mount Inspection (`System.configuration`):**
  - `cores` (`CPU`): physical/logical core counts with safe fallback when `psutil.cpu_count(logical=False)` returns `None`.
  - `memory`: total, available, and usage metrics.
  - `drives` (`DriveGroup` / `Drive`): resilient mount inspection that safely skips unreadable FUSE mounts and unready removable Windows drives instead of crashing on `PermissionError`/`OSError`.
- **Container-Safe User Inspection (`System.users`):** current user, home directory, and active user listing with fallback when `psutil.users()` is unavailable in containers.

## Usage

```python
from werkflow_system import System, Linux, OperatingSystemType

system = System()
print(system.os.type, system.os.name, system.architecture)
print(system.configuration.cores.physical)

if isinstance(system.os, Linux):
    print(system.os.family, system.os.package_manager)
```

## Dependencies

- `werkflow-core`
- `psutil`
- `distro`

## Requirements

- Python `>=3.11`
