from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_metric_result_v2 import ConnectMetricResultV2


class ConnectGetMetricDataV2Response(BaseModel):
    NextToken: StrictStr | None = None
    MetricResults: list[ConnectMetricResultV2] | None = None
    ResponseMetadata: dict[str, Any] | None = None
