from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_commit_repository_trigger import CodeCommitRepositoryTrigger


class CodeCommitGetRepositoryTriggersResponse(BaseModel):
    configurationId: StrictStr | None = None
    triggers: list[CodeCommitRepositoryTrigger] | None = None
    ResponseMetadata: dict[str, Any] | None = None
