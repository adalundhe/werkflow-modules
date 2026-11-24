from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_hash_key_range import KinesisHashKeyRange


class KinesisChildShard(BaseModel):
    ShardId: StrictStr | None = None
    ParentShards: list[StrictStr] | None = None
    HashKeyRange: KinesisHashKeyRange | None = None
