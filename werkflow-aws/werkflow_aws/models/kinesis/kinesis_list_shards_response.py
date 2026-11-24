from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kinesis_shard import KinesisShard


class KinesisListShardsResponse(BaseModel):
    Shards: list[KinesisShard] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
