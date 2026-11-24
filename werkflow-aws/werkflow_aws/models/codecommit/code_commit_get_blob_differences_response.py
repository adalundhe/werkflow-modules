from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .code_commit_diff_hunk import CodeCommitDiffHunk


class CodeCommitGetBlobDifferencesResponse(BaseModel):
    hunks: list[CodeCommitDiffHunk] | None = None
    isBinary: StrictBool | None = None
    beforeBlobSize: StrictInt | None = None
    afterBlobSize: StrictInt | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
