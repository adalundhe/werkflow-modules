from __future__ import annotations
from pydantic import BaseModel
from .open_search_availability_zone_info import OpenSearchAvailabilityZoneInfo


class OpenSearchEnvironmentInfo(BaseModel):
    AvailabilityZoneInformation: list[OpenSearchAvailabilityZoneInfo] | None = None
