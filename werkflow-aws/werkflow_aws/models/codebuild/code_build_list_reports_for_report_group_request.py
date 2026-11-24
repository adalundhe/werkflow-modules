from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .code_build_report_filter import CodeBuildReportFilter


class CodeBuildListReportsForReportGroupRequest(BaseModel):
    reportGroupArn: StrictStr
    nextToken: StrictStr | None = None
    sortOrder: Literal['ASCENDING', 'DESCENDING'] | None = None
    maxResults: StrictInt | None = None
    filter: CodeBuildReportFilter | None = None
