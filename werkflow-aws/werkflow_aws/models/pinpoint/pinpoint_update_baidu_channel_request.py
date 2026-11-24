from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_baidu_channel_request import PinpointBaiduChannelRequest


class PinpointUpdateBaiduChannelRequest(BaseModel):
    ApplicationId: StrictStr
    BaiduChannelRequest: PinpointBaiduChannelRequest
