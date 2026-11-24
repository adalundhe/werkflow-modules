from __future__ import annotations
from pydantic import BaseModel
from .connect_participant_timer_configuration import ConnectParticipantTimerConfiguration


class ConnectChatParticipantRoleConfig(BaseModel):
    ParticipantTimerConfigList: list[ConnectParticipantTimerConfiguration]
