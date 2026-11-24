from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_adm_channel_response import PinpointADMChannelResponse


class PinpointUpdateAdmChannelResponse(BaseModel):
    ADMChannelResponse: PinpointADMChannelResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
