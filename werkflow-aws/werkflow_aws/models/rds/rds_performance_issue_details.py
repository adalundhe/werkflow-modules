from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .rds_metric import RDSMetric


class RDSPerformanceIssueDetails(BaseModel):
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    Metrics: list[RDSMetric] | None = None
    Analysis: StrictStr | None = None
