from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_send_users_message_request import PinpointSendUsersMessageRequest


class PinpointSendUsersMessagesRequest(BaseModel):
    ApplicationId: StrictStr
    SendUsersMessageRequest: PinpointSendUsersMessageRequest
