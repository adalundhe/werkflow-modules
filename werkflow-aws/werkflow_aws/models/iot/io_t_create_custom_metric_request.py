from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .io_t_tag import IoTTag


class IoTCreateCustomMetricRequest(BaseModel):
    metricName: StrictStr
    metricType: Literal['string-list', 'ip-address-list', 'number-list', 'number']
    clientRequestToken: StrictStr
    displayName: StrictStr | None = None
    tags: list[IoTTag] | None = None
