from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .kinesis_child_shard import KinesisChildShard
from .kinesis_record import KinesisRecord


class KinesisGetRecordsResponse(BaseModel):
    Records: list[KinesisRecord] | None = None
    NextShardIterator: StrictStr | None = None
    MillisBehindLatest: StrictInt | None = None
    ChildShards: list[KinesisChildShard] | None = None
    ResponseMetadata: dict[str, Any] | None = None
