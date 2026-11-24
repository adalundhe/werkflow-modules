from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_current_metric_result import ConnectCurrentMetricResult


class ConnectGetCurrentMetricDataResponse(BaseModel):
    NextToken: StrictStr | None = None
    MetricResults: list[ConnectCurrentMetricResult] | None = None
    DataSnapshotTime: datetime.datetime | StrictStr | None = None
    ApproximateTotalCount: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
