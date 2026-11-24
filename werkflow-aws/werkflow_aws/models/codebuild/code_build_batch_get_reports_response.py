from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_build_report import CodeBuildReport


class CodeBuildBatchGetReportsResponse(BaseModel):
    reports: list[CodeBuildReport] | None = None
    reportsNotFound: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
