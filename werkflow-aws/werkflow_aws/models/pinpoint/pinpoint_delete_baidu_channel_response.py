from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_baidu_channel_response import PinpointBaiduChannelResponse


class PinpointDeleteBaiduChannelResponse(BaseModel):
    BaiduChannelResponse: PinpointBaiduChannelResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
