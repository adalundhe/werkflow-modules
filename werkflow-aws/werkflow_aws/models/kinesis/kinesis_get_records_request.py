from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class KinesisGetRecordsRequest(BaseModel):
    ShardIterator: StrictStr
    Limit: StrictInt | None = None
    StreamARN: StrictStr | None = None
    StreamId: StrictStr | None = None
    DryRun: StrictBool | None = None
