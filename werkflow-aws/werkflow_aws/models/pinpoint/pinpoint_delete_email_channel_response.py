from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_email_channel_response import PinpointEmailChannelResponse


class PinpointDeleteEmailChannelResponse(BaseModel):
    EmailChannelResponse: PinpointEmailChannelResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
