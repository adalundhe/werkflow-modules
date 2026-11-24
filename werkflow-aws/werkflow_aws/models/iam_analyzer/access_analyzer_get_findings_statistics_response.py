from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .access_analyzer_findings_statistics import AccessAnalyzerFindingsStatistics


class AccessAnalyzerGetFindingsStatisticsResponse(BaseModel):
    findingsStatistics: list[AccessAnalyzerFindingsStatistics] | None = None
    lastUpdatedAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
