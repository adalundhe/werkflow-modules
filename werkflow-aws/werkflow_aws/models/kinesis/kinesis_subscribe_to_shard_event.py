from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .kinesis_child_shard import KinesisChildShard
from .kinesis_record import KinesisRecord


class KinesisSubscribeToShardEvent(BaseModel):
    Records: list[KinesisRecord] | None = None
    ContinuationSequenceNumber: StrictStr | None = None
    MillisBehindLatest: StrictInt | None = None
    ChildShards: list[KinesisChildShard] | None = None
