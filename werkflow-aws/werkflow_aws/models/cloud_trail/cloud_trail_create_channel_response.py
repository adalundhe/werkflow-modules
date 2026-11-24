from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_trail_destination import CloudTrailDestination
from .cloud_trail_tag import CloudTrailTag


class CloudTrailCreateChannelResponse(BaseModel):
    ChannelArn: StrictStr | None = None
    Name: StrictStr | None = None
    Source: StrictStr | None = None
    Destinations: list[CloudTrailDestination] | None = None
    Tags: list[CloudTrailTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
