from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_commit_difference import CodeCommitDifference


class CodeCommitGetDifferencesResponse(BaseModel):
    differences: list[CodeCommitDifference] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
