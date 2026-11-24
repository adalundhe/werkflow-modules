from __future__ import annotations
from pydantic import BaseModel
from .pinpoint_number_validate_request import PinpointNumberValidateRequest


class PinpointPhoneNumberValidateRequest(BaseModel):
    NumberValidateRequest: PinpointNumberValidateRequest
