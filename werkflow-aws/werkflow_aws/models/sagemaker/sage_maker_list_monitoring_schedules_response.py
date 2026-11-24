from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_monitoring_schedule_summary import SageMakerMonitoringScheduleSummary


class SageMakerListMonitoringSchedulesResponse(BaseModel):
    MonitoringScheduleSummaries: list[SageMakerMonitoringScheduleSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
