from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .connect_participant_timer_value import ConnectParticipantTimerValue


class ConnectParticipantTimerConfiguration(BaseModel):
    ParticipantRole: Literal['CUSTOMER', 'AGENT']
    TimerType: Literal['IDLE', 'DISCONNECT_NONCUSTOMER']
    TimerValue: ConnectParticipantTimerValue
