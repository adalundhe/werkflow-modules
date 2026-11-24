from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_hash_key_range import KinesisHashKeyRange
from .kinesis_sequence_number_range import KinesisSequenceNumberRange


class KinesisShard(BaseModel):
    ShardId: StrictStr | None = None
    ParentShardId: StrictStr | None = None
    AdjacentParentShardId: StrictStr | None = None
    HashKeyRange: KinesisHashKeyRange | None = None
    SequenceNumberRange: KinesisSequenceNumberRange | None = None
