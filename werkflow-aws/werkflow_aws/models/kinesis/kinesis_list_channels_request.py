from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .kinesis_stream_filter import KinesisStreamFilter


class KinesisListChannelsRequest(BaseModel):
    StreamFilter: list[KinesisStreamFilter] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
