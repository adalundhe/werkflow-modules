from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .kinesis_starting_position import KinesisStartingPosition


class KinesisSubscribeToShardRequest(BaseModel):
    ConsumerARN: StrictStr
    ShardId: StrictStr
    StartingPosition: KinesisStartingPosition
    StreamId: StrictStr | None = None
    DryRun: StrictBool | None = None
