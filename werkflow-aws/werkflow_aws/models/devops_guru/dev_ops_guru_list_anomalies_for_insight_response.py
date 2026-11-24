from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dev_ops_guru_proactive_anomaly_summary import DevOpsGuruProactiveAnomalySummary
from .dev_ops_guru_reactive_anomaly_summary import DevOpsGuruReactiveAnomalySummary


class DevOpsGuruListAnomaliesForInsightResponse(BaseModel):
    ProactiveAnomalies: list[DevOpsGuruProactiveAnomalySummary] | None = None
    ReactiveAnomalies: list[DevOpsGuruReactiveAnomalySummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
