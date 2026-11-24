from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchStartMetricStreamsRequest(BaseModel):
    Names: list[StrictStr]
