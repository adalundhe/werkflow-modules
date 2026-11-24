from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_trail_destination import CloudTrailDestination
from .cloud_trail_tag import CloudTrailTag


class CloudTrailCreateChannelRequest(BaseModel):
    Name: StrictStr
    Source: StrictStr
    Destinations: list[CloudTrailDestination]
    Tags: list[CloudTrailTag] | None = None
