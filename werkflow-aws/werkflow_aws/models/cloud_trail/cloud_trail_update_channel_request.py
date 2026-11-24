from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_trail_destination import CloudTrailDestination


class CloudTrailUpdateChannelRequest(BaseModel):
    Channel: StrictStr
    Destinations: list[CloudTrailDestination] | None = None
    Name: StrictStr | None = None
