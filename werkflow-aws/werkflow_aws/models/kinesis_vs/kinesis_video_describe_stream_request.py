from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisVideoDescribeStreamRequest(BaseModel):
    StreamName: StrictStr | None = None
    StreamARN: StrictStr | None = None
