from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class KinesisUpdateStreamRecordDistributionStrategyRequest(BaseModel):
    StreamARN: StrictStr
    RecordDistributionStrategy: Literal['AUTO', 'USER_PARTITION_KEY']
    StreamId: StrictStr | None = None
