from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .kinesis_stream_mode_details import KinesisStreamModeDetails


class KinesisCreateStreamRequest(BaseModel):
    StreamName: StrictStr
    ShardCount: StrictInt | None = None
    StreamModeDetails: KinesisStreamModeDetails | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    WarmThroughputMiBps: StrictInt | None = None
    MaxRecordSizeInKiB: StrictInt | None = None
    RecordDistributionStrategy: Literal['AUTO', 'USER_PARTITION_KEY'] | None = None
