from __future__ import annotations
from pydantic import BaseModel
from .pinpoint_endpoint_response import PinpointEndpointResponse


class PinpointEndpointsResponse(BaseModel):
    Item: list[PinpointEndpointResponse] | None = None
