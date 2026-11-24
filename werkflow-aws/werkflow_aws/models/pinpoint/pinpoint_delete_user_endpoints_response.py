from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_endpoints_response import PinpointEndpointsResponse


class PinpointDeleteUserEndpointsResponse(BaseModel):
    EndpointsResponse: PinpointEndpointsResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
