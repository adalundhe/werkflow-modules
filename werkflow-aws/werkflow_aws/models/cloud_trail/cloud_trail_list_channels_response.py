from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_trail_channel import CloudTrailChannel


class CloudTrailListChannelsResponse(BaseModel):
    Channels: list[CloudTrailChannel] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
