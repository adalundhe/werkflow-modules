from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_send_users_message_response import PinpointSendUsersMessageResponse


class PinpointSendUsersMessagesResponse(BaseModel):
    SendUsersMessageResponse: PinpointSendUsersMessageResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
