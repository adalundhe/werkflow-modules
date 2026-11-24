from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .msk_channel_info import MSKChannelInfo


class MSKListChannelsResponse(BaseModel):
    Channels: list[MSKChannelInfo] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
