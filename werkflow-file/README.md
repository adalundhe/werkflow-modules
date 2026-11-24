# werkflow-file

Version `0.2.0`

Asynchronous file reading, writing, transformation, and recursive file discovery module for [Werkflow](https://github.com/adalundhe/werkflow).

## Installation

```bash
pip install werkflow-file
```

## Features

- **Typed Text & Binary I/O:** Overloaded `read(path, mode='r'|'rb', encoding='utf-8')` and `write(path, data, transform=..., mode='w'|'wb'|'a'|'ab', encoding='utf-8')` backed by a thread pool executor.
- **Transform Pipelines:** Pass any typed `transform` callable to serialize structured objects directly to `str` or `bytes` during `write()`.
- **Recursive Search:** `list_matching_files(path, pattern)` resolves relative/tilde paths via `werkflow-shell` and returns matching file paths via `pathlib.Path.rglob`.
- **Safe First-Call Execution & Lifecycle:** Lazily binds the running event loop on every call and supports `async with File() as f:`, `await f.close()`, and `f.abort()`.

## Usage

```python
import json
from werkflow_file import File

async with File() as files:
    await files.write("config.json", {"debug": False}, transform=json.dumps)
    raw = await files.read("config.json")
    py_files = await files.list_matching_files(".", "*.py")
```

## Dependencies

- `werkflow-core`
- `werkflow-shell`
- `werkflow-system`

## Requirements

- Python `>=3.11`
