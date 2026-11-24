from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_number_validate_response import PinpointNumberValidateResponse


class PinpointPhoneNumberValidateResponse(BaseModel):
    NumberValidateResponse: PinpointNumberValidateResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
