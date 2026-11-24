# werkflow-python

Version `0.2.0`

Cross-platform asynchronous Python virtual environment and `pip` dependency management module for [Werkflow](https://github.com/adalundhe/werkflow).

## Installation

```bash
pip install werkflow-python
```

## Features

- **Cross-Platform Virtual Environments:** `create_venv()` and `activate_virtual_environment()` resolve `bin/` on POSIX and `Scripts/` on Windows and update `PATH` and `VIRTUAL_ENV` directly without shell-specific `source` commands.
- **Package Installation:** `install_requirements()` and `install_requirements_from_file()` invoke the target environment's `pip` executable directly with properly separated arguments.
- **Version Selection:** `set_python_version()` configures the target Python interpreter/version.
- **Async Lifecycle:** Supports `async with Python() as py:`, `await py.close()`, and `py.abort()`.

## Usage

```python
from werkflow_python import Python

async with Python() as py:
    await py.create_venv("./.venv")
    await py.install_requirements(["pydantic", "pytest"], venv_path="./.venv")
    await py.install_requirements_from_file("requirements.txt", venv_path="./.venv")
```

## Dependencies

- `werkflow-core`
- `werkflow-shell`
- `werkflow-system`

## Requirements

- Python `>=3.11`
