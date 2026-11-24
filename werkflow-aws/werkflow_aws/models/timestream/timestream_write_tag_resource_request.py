from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .timestream_write_tag import TimestreamWriteTag


class TimestreamWriteTagResourceRequest(BaseModel):
    ResourceARN: StrictStr
    Tags: list[TimestreamWriteTag]
