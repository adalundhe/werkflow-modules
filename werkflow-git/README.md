# werkflow-git

Version `0.3.0`

Asynchronous Git repository automation module for [Werkflow](https://github.com/adalundhe/werkflow), powered by GitPython.

## Installation

```bash
pip install werkflow-git
```

## Features

- **Repository Initialization & Discovery:** `init()`, `clone()`, `reinitialize()`, `check_if_repo_exists()`, and `set_gitignore()`.
- **Branch & Remote Management:** `checkout()`, `set_remote()`, `reinitialize_remote()`, and `check_remote_is_set()`.
- **Working Tree & Sync Operations:** `add()`, `commit()`, `fetch()`, `pull()`, and `push()` executed asynchronously off the event loop.
- **Clean Resource Handling:** Properly closes GitPython repository handles in `close()` and `abort()`.

## Usage

```python
from werkflow_git import Git

async with Git() as git:
    await git.init("./my-repo")
    await git.add("./my-repo", ["README.md"])
    await git.commit("./my-repo", "Initial commit")
    await git.set_remote("./my-repo", "origin", "https://github.com/org/repo.git")
```

## Dependencies

- `werkflow-core`
- `werkflow-shell`
- `werkflow-system`
- `gitpython`

## Requirements

- Python `>=3.11`
- `git` CLI available on `PATH`
