from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .timestream_query_tag import TimestreamQueryTag


class TimestreamQueryTagResourceRequest(BaseModel):
    ResourceARN: StrictStr
    Tags: list[TimestreamQueryTag]
