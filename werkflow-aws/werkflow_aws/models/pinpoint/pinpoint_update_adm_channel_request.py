from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_adm_channel_request import PinpointADMChannelRequest


class PinpointUpdateAdmChannelRequest(BaseModel):
    ADMChannelRequest: PinpointADMChannelRequest
    ApplicationId: StrictStr
