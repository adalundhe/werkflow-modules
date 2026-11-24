# werkflow-modules

Official collection of composable, strictly-typed modules for [Werkflow](https://github.com/adalundhe/werkflow).

Every module subclasses `werkflow_core.Module`, is zero-argument constructible for automatic Werkflow graph discovery, exposes async `close()` and sync `abort()` lifecycle hooks, and targets Python `>=3.11` with strict type checking and Pydantic v2 validation.

## Modules

| Package | Version | Import | Description |
| --- | --- | --- | --- |
| [`werkflow-core`](./werkflow-core/README.md) | `0.2.0` | `werkflow_core` | Base `Module` contract, async context manager, and `MissingModuleError` |
| [`werkflow-system`](./werkflow-system/README.md) | `0.4.0` | `werkflow_system` | Cross-platform OS, Linux distro family, CPU/RAM/drive, architecture, and user inspection |
| [`werkflow-shell`](./werkflow-shell/README.md) | `0.2.0` | `werkflow_shell` | Cross-platform async shell runner (macOS, Linux distros, Windows PowerShell/CMD) |
| [`werkflow-file`](./werkflow-file/README.md) | `0.2.0` | `werkflow_file` | Async text/binary file I/O and recursive glob search |
| [`werkflow-git`](./werkflow-git/README.md) | `0.3.0` | `werkflow_git` | Async Git repository automation built on GitPython |
| [`werkflow-python`](./werkflow-python/README.md) | `0.2.0` | `werkflow_python` | Cross-platform virtual environment management and `pip` package installation |
| [`werkflow-encryption`](./werkflow-encryption/README.md) | `0.3.0` | `werkflow_encryption` | Async Fernet, AES-256-GCM, and NaCl SealedBox encryption with key management |
| [`werkflow-secrets`](./werkflow-secrets/README.md) | `0.3.0` | `werkflow_secrets` | Encrypted secret storage and retrieval for environment variables, files, and JSON |
| [`werkflow-http`](./werkflow-http/README.md) | `0.7.0` | `werkflow_http` | Async HTTP/1.1 client with DNS caching, TLS verification, cookies, redirects, and multipart uploads |
| [`werkflow-aws`](./werkflow-aws/README.md) | `0.7.0` | `werkflow_aws` | Strictly-typed async AWS SDK wrapper covering 20 AWS services (2,548 boto3 ops + 514 paginators) |
| [`werkflow-docker`](./werkflow-docker/README.md) | `0.4.0` | `werkflow_docker` | Async Docker SDK client, CLI build options, and fluent Dockerfile `Image` builder |
| [`werkflow-github`](./werkflow-github/README.md) | `0.3.0` | `werkflow_github` | Async GitHub REST API client for repos, PRs, Actions workflows, secrets, and variables |
| [`werkflow-jira`](./werkflow-jira/README.md) | `0.4.0` | `werkflow_jira` | Async Jira Cloud REST API client with Atlassian Document Format (ADF) content builders |
| [`werkflow-appito`](./werkflow-appito/README.md) | `0.2.0` | `werkflow_appito` | Async Apptio Frontdoor authentication and `.csv`/`.csv.gz` dataset upload client |
| [`werkflow-metrikflow`](./werkflow-metrikflow/README.md) | `0.3.0` | `werkflow_metrikflow` | Optional Metrikflow metrics sender/loader integration for Werkflow workflows |

## Installation

Install individual modules directly:

```bash
pip install werkflow-shell werkflow-aws
```

Or install via Werkflow extras:

```bash
pip install "werkflow[aws,docker,github]"
pip install "werkflow[all]"
```

## Using Modules in a Werkflow

```python
from werkflow import Workflow, requires, step
from werkflow_shell import Shell
from werkflow_file import File


@requires(Shell, File)
class BuildWorkflow(Workflow):
    def __init__(self) -> None:
        super().__init__()
        self.shell = Shell()
        self.file = File()

    @step()
    async def inspect(self) -> dict[str, str]:
        cwd = await self.shell.get_current_directory()
        return {"cwd": cwd}

    async def close(self) -> None:
        await self.file.close()
        await self.shell.close()
```

## Requirements

- Python `>=3.11`
- License: MIT
