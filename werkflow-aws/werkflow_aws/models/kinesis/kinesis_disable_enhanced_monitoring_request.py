from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class KinesisDisableEnhancedMonitoringRequest(BaseModel):
    ShardLevelMetrics: list[Literal['IncomingBytes', 'IncomingRecords', 'OutgoingBytes', 'OutgoingRecords', 'WriteProvisionedThroughputExceeded', 'ReadProvisionedThroughputExceeded', 'IteratorAgeMilliseconds', 'ALL']]
    StreamName: StrictStr | None = None
    StreamARN: StrictStr | None = None
    StreamId: StrictStr | None = None
