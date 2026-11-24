from __future__ import annotations
from pydantic import BaseModel
from .code_commit_conflict_metadata import CodeCommitConflictMetadata
from .code_commit_merge_hunk import CodeCommitMergeHunk


class CodeCommitConflict(BaseModel):
    conflictMetadata: CodeCommitConflictMetadata | None = None
    mergeHunks: list[CodeCommitMergeHunk] | None = None
