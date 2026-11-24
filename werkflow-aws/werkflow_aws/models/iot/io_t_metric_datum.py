from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .io_t_metric_value import IoTMetricValue


class IoTMetricDatum(BaseModel):
    timestamp: datetime.datetime | StrictStr | None = None
    value: IoTMetricValue | None = None
