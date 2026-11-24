from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .code_commit_merge_hunk_detail import CodeCommitMergeHunkDetail


class CodeCommitMergeHunk(BaseModel):
    isConflict: StrictBool | None = None
    source: CodeCommitMergeHunkDetail | None = None
    destination: CodeCommitMergeHunkDetail | None = None
    base: CodeCommitMergeHunkDetail | None = None
