from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisSplitShardRequest(BaseModel):
    ShardToSplit: StrictStr
    NewStartingHashKey: StrictStr
    StreamName: StrictStr | None = None
    StreamARN: StrictStr | None = None
    StreamId: StrictStr | None = None
