from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_queue_starting_position import KinesisQueueStartingPosition


class KinesisQueueStreamConfiguration(BaseModel):
    StreamARN: StrictStr | None = None
    StartingPosition: KinesisQueueStartingPosition | None = None
