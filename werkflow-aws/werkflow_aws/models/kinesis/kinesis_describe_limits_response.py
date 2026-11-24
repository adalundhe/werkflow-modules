from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt


class KinesisDescribeLimitsResponse(BaseModel):
    ShardLimit: StrictInt | None = None
    OpenShardCount: StrictInt | None = None
    OnDemandStreamCount: StrictInt | None = None
    OnDemandStreamCountLimit: StrictInt | None = None
    ChannelCount: StrictInt | None = None
    ChannelCountLimit: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
