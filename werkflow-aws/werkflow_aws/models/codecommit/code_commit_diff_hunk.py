from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .code_commit_diff_change import CodeCommitDiffChange


class CodeCommitDiffHunk(BaseModel):
    beforeStartLine: StrictInt | None = None
    beforeLineCount: StrictInt | None = None
    afterStartLine: StrictInt | None = None
    afterLineCount: StrictInt | None = None
    changes: list[CodeCommitDiffChange] | None = None
