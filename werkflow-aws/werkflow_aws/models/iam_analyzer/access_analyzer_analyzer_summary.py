from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .access_analyzer_analyzer_configuration import AccessAnalyzerAnalyzerConfiguration
from .access_analyzer_status_reason import AccessAnalyzerStatusReason


class AccessAnalyzerAnalyzerSummary(BaseModel):
    arn: StrictStr | None = None
    name: StrictStr | None = None
    type: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    lastResourceAnalyzed: StrictStr | None = None
    lastResourceAnalyzedAt: datetime.datetime | StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    status: StrictStr | None = None
    statusReason: AccessAnalyzerStatusReason | None = None
    configuration: AccessAnalyzerAnalyzerConfiguration | None = None
    managedBy: StrictStr | None = None
