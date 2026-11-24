from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_commit_repository_trigger_execution_failure import CodeCommitRepositoryTriggerExecutionFailure


class CodeCommitTestRepositoryTriggersResponse(BaseModel):
    successfulExecutions: list[StrictStr] | None = None
    failedExecutions: list[CodeCommitRepositoryTriggerExecutionFailure] | None = None
    ResponseMetadata: dict[str, Any] | None = None
