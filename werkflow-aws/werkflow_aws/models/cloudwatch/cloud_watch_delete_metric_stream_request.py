from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchDeleteMetricStreamRequest(BaseModel):
    Name: StrictStr
