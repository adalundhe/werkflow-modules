from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cost_explorer_anomaly import CostExplorerAnomaly


class CostExplorerGetAnomaliesResponse(BaseModel):
    Anomalies: list[CostExplorerAnomaly] | None = None
    NextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
