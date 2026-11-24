from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_build_report_group_trend_stats import CodeBuildReportGroupTrendStats
from .code_build_report_with_raw_data import CodeBuildReportWithRawData


class CodeBuildGetReportGroupTrendResponse(BaseModel):
    stats: CodeBuildReportGroupTrendStats | None = None
    rawData: list[CodeBuildReportWithRawData] | None = None
    ResponseMetadata: dict[str, Any] | None = None
