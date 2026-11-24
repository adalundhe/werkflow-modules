from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from typing import Any
from .cloud_watch_metric_datum import CloudWatchMetricDatum


class CloudWatchPutMetricDataRequest(BaseModel):
    Namespace: StrictStr | None = None
    MetricData: list[CloudWatchMetricDatum] | None = None
    EntityMetricData: list[dict[str, Any]] | None = None
    StrictEntityValidation: StrictBool | None = None
