from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisMergeShardsRequest(BaseModel):
    ShardToMerge: StrictStr
    AdjacentShardToMerge: StrictStr
    StreamName: StrictStr | None = None
    StreamARN: StrictStr | None = None
    StreamId: StrictStr | None = None
