from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .code_commit_conflict_metadata import CodeCommitConflictMetadata


class CodeCommitGetMergeConflictsResponse(BaseModel):
    mergeable: StrictBool | None = None
    destinationCommitId: StrictStr | None = None
    sourceCommitId: StrictStr | None = None
    baseCommitId: StrictStr | None = None
    conflictMetadataList: list[CodeCommitConflictMetadata] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
