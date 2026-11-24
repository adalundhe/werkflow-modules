from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisDescribeStreamRequest(BaseModel):
    StreamName: StrictStr | None = None
    Limit: StrictInt | None = None
    ExclusiveStartShardId: StrictStr | None = None
    StreamARN: StrictStr | None = None
    StreamId: StrictStr | None = None
