from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ConnectCreateMetricResponse(BaseModel):
    MetricArn: StrictStr | None = None
    MetricId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
