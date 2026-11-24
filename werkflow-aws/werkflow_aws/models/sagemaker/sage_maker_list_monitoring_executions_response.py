from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_monitoring_execution_summary import SageMakerMonitoringExecutionSummary


class SageMakerListMonitoringExecutionsResponse(BaseModel):
    MonitoringExecutionSummaries: list[SageMakerMonitoringExecutionSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
