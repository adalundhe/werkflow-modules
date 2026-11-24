# werkflow-core

Version `0.2.0`

Core base abstractions and exception types shared by all [Werkflow](https://github.com/adalundhe/werkflow) modules.

## Installation

```bash
pip install werkflow-core
```

## Overview

`werkflow-core` defines the contract every Werkflow module implements so Werkflow can discover, validate (`@requires`), instantiate, and cleanly shut down modules:

- `Module`: Base class declaring `module_enabled: ClassVar[bool]`, `dependencies: ClassVar[Sequence[str]]`, async context manager support (`__aenter__` / `__aexit__`), `async def close()`, and `def abort()`.
- `MissingModuleError`: Raised when a module with missing optional dependencies is instantiated or required by a workflow.

## Usage

```python
from werkflow_core import Module, MissingModuleError


class CustomModule(Module):
    module_enabled = True
    dependencies = ["httpx"]

    async def close(self) -> None:
        ...

    def abort(self) -> None:
        ...
```

## Requirements

- Python `>=3.11`
- No external runtime dependencies
