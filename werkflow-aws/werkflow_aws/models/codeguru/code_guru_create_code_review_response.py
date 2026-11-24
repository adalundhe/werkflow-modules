from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_guru_code_review import CodeGuruCodeReview


class CodeGuruCreateCodeReviewResponse(BaseModel):
    CodeReview: CodeGuruCodeReview | None = None
    ResponseMetadata: dict[str, Any] | None = None
