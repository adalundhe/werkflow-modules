from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class KinesisGetShardIteratorRequest(BaseModel):
    ShardId: StrictStr
    ShardIteratorType: Literal['AT_SEQUENCE_NUMBER', 'AFTER_SEQUENCE_NUMBER', 'TRIM_HORIZON', 'LATEST', 'AT_TIMESTAMP']
    StreamName: StrictStr | None = None
    StartingSequenceNumber: StrictStr | None = None
    Timestamp: datetime.datetime | StrictStr | None = None
    StreamARN: StrictStr | None = None
    StreamId: StrictStr | None = None
    DryRun: StrictBool | None = None
