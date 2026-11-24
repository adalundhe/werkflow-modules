from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_endpoint_response import PinpointEndpointResponse


class PinpointGetEndpointResponse(BaseModel):
    EndpointResponse: PinpointEndpointResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
