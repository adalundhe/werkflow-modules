from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_build_report_group import CodeBuildReportGroup


class CodeBuildBatchGetReportGroupsResponse(BaseModel):
    reportGroups: list[CodeBuildReportGroup] | None = None
    reportGroupsNotFound: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
