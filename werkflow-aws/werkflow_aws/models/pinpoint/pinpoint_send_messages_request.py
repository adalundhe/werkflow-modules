from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_message_request import PinpointMessageRequest


class PinpointSendMessagesRequest(BaseModel):
    ApplicationId: StrictStr
    MessageRequest: PinpointMessageRequest
