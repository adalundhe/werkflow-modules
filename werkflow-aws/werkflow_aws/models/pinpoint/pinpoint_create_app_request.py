from __future__ import annotations
from pydantic import BaseModel
from .pinpoint_create_application_request import PinpointCreateApplicationRequest


class PinpointCreateAppRequest(BaseModel):
    CreateApplicationRequest: PinpointCreateApplicationRequest
