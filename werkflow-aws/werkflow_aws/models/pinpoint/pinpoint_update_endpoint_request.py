from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_endpoint_request import PinpointEndpointRequest


class PinpointUpdateEndpointRequest(BaseModel):
    ApplicationId: StrictStr
    EndpointId: StrictStr
    EndpointRequest: PinpointEndpointRequest
