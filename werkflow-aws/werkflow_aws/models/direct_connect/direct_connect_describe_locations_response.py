from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .direct_connect_location import DirectConnectLocation


class DirectConnectDescribeLocationsResponse(BaseModel):
    locations: list[DirectConnectLocation] | None = None
    ResponseMetadata: dict[str, Any] | None = None
