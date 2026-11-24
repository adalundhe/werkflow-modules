from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .code_commit_conflict_resolution import CodeCommitConflictResolution


class CodeCommitMergePullRequestBySquashRequest(BaseModel):
    pullRequestId: StrictStr
    repositoryName: StrictStr
    sourceCommitId: StrictStr | None = None
    conflictDetailLevel: Literal['FILE_LEVEL', 'LINE_LEVEL'] | None = None
    conflictResolutionStrategy: Literal['NONE', 'ACCEPT_SOURCE', 'ACCEPT_DESTINATION', 'AUTOMERGE'] | None = None
    commitMessage: StrictStr | None = None
    authorName: StrictStr | None = None
    email: StrictStr | None = None
    keepEmptyFolders: StrictBool | None = None
    conflictResolution: CodeCommitConflictResolution | None = None
