# werkflow-github

Version `0.3.0`

Asynchronous GitHub REST API automation module for [Werkflow](https://github.com/adalundhe/werkflow).

## Installation

```bash
pip install werkflow-github
```

## Features

- **Authentication:** Personal access token / GitHub token login via `login()`.
- **Repositories & Security:** `get_repo()`, `check_if_repo_exists()`, `create_repo()`, `create_organization_repo()`, `list_organization_repositories()`, `set_branch_protections()`, `set_automated_security_fixes()`, and `set_vulnerability_reports()`.
- **Pull Requests:** `create_pull_request()`, `get_pull_request()`, `list_pull_requests()`, and `list_pull_request_commits()` returning typed `PullRequest` models.
- **GitHub Actions:** `get_workflow()`, `list_workflow_runs()`, `get_workflow_run()`, and `get_workflow_run_jobs()` returning typed `Workflow`, `Run`, `Job`, and `Step` models.
- **Encrypted Secrets & Variables:** `get_repository_public_key()`, `add_or_update_repository_secret()` (encrypts values with NaCl SealedBox via `werkflow-encryption`), `get_repository_secret()`, `list_repository_secrets()`, `delete_repository_secret()`, `add_repository_variable()`, `update_repository_variable()`, `get_repository_variable()`, `list_repository_variables()`, and `delete_repository_variable()`.

## Usage

```python
from werkflow_github import Github

async with Github() as gh:
    await gh.login(token="ghp_...")
    repo = await gh.get_repo("my-org", "my-repo")
    prs = await gh.list_pull_requests("my-org", "my-repo")
    await gh.add_or_update_repository_secret("my-org", "my-repo", "DEPLOY_KEY", "secret-value")
```

## Dependencies

- `werkflow-core`
- `werkflow-encryption`
- `werkflow-http`
- `werkflow-system`
- `pydantic`

## Requirements

- Python `>=3.11`
