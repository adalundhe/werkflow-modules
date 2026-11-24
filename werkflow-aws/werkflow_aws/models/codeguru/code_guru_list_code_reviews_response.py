from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_guru_code_review_summary import CodeGuruCodeReviewSummary


class CodeGuruListCodeReviewsResponse(BaseModel):
    CodeReviewSummaries: list[CodeGuruCodeReviewSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
