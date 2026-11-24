from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .code_build_report_filter import CodeBuildReportFilter


class CodeBuildListReportsRequest(BaseModel):
    sortOrder: Literal['ASCENDING', 'DESCENDING'] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    filter: CodeBuildReportFilter | None = None
