from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchStopMetricStreamsRequest(BaseModel):
    Names: list[StrictStr]
