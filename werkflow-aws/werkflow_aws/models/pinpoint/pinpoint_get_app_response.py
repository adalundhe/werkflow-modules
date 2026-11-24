from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_application_response import PinpointApplicationResponse


class PinpointGetAppResponse(BaseModel):
    ApplicationResponse: PinpointApplicationResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
