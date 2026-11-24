from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_commit_repository_trigger import CodeCommitRepositoryTrigger


class CodeCommitPutRepositoryTriggersRequest(BaseModel):
    repositoryName: StrictStr
    triggers: list[CodeCommitRepositoryTrigger]
