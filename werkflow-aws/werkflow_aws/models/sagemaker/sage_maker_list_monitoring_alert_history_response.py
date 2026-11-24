from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_monitoring_alert_history_summary import SageMakerMonitoringAlertHistorySummary


class SageMakerListMonitoringAlertHistoryResponse(BaseModel):
    MonitoringAlertHistory: list[SageMakerMonitoringAlertHistorySummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
