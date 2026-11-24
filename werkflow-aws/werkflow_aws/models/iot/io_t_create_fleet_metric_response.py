from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class IoTCreateFleetMetricResponse(BaseModel):
    metricName: StrictStr | None = None
    metricArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
