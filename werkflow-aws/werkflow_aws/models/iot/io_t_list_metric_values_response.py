from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_metric_datum import IoTMetricDatum


class IoTListMetricValuesResponse(BaseModel):
    metricDatumList: list[IoTMetricDatum] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
