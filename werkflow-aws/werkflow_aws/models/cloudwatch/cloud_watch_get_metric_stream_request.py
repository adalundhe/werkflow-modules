from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchGetMetricStreamRequest(BaseModel):
    Name: StrictStr
