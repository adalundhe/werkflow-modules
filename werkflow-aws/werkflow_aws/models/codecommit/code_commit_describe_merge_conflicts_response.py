from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_commit_conflict_metadata import CodeCommitConflictMetadata
from .code_commit_merge_hunk import CodeCommitMergeHunk


class CodeCommitDescribeMergeConflictsResponse(BaseModel):
    conflictMetadata: CodeCommitConflictMetadata | None = None
    mergeHunks: list[CodeCommitMergeHunk] | None = None
    nextToken: StrictStr | None = None
    destinationCommitId: StrictStr | None = None
    sourceCommitId: StrictStr | None = None
    baseCommitId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
