# werkflow-jira

Version `0.4.0`

Asynchronous Jira Cloud REST API v3 client with typed Atlassian Document Format (ADF) builders for [Werkflow](https://github.com/adalundhe/werkflow).

## Installation

```bash
pip install werkflow-jira
```

## Features

- **Issues & Batch Creation:** `create_issue()`, `create_issue_batch()`, `get_issue()`, and `create_issue_link()`.
- **Project & Metadata Lookup:** `get_jira_project()`, `get_project_issue_types()`, `get_matching_project_issue_type()`, `list_priorities()`, `get_matching_priority()`, `get_issue_link_types()`, `get_matching_issue_link_type()`, and `get_matching_user_by_email()`.
- **Typed ADF Content Builders:** Compose rich issue descriptions with validated Pydantic v2 models (`JiraTopLevelBlock`, `JiraChildBlock`, `JiraInlineBlock`, `ParagraphAttrs`, `HeadingAttrs`, `PanelAttrs`, `TableAttrs`, `MentionAttrs`, `LinkMarkAttrs`, etc.) and the `Issue` builder.
- **Typed Error Handling:** Maps HTTP errors to `BadRequestError`, `UnauthorizedRequestError`, `ResourceNotFoundError`, `MethodNotAllowedError`, `UnprocessableContentError`, and `ServerFailedError`.

## Usage

```python
from werkflow_jira import Jira

async with Jira() as jira:
    project = await jira.get_jira_project(
        organization="my-org",
        project_key="ENG",
        email="bot@example.com",
        api_token="jira-api-token",
    )
    priorities = await jira.list_priorities(
        organization="my-org",
        email="bot@example.com",
        api_token="jira-api-token",
    )
```

## Dependencies

- `werkflow-core`
- `werkflow-http`
- `pydantic`

## Requirements

- Python `>=3.11`
