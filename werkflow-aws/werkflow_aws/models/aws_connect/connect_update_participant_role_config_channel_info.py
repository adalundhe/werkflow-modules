from __future__ import annotations
from pydantic import BaseModel
from .connect_chat_participant_role_config import ConnectChatParticipantRoleConfig


class ConnectUpdateParticipantRoleConfigChannelInfo(BaseModel):
    Chat: ConnectChatParticipantRoleConfig | None = None
