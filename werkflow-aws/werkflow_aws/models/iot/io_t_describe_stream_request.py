from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDescribeStreamRequest(BaseModel):
    streamId: StrictStr
