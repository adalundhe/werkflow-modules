from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_build_report_group import CodeBuildReportGroup


class CodeBuildUpdateReportGroupResponse(BaseModel):
    reportGroup: CodeBuildReportGroup | None = None
    ResponseMetadata: dict[str, Any] | None = None
