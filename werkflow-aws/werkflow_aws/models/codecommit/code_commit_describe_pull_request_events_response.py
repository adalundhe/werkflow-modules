from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_commit_pull_request_event import CodeCommitPullRequestEvent


class CodeCommitDescribePullRequestEventsResponse(BaseModel):
    pullRequestEvents: list[CodeCommitPullRequestEvent] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
