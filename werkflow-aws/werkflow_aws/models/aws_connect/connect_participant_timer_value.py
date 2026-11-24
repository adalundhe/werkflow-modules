from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt


class ConnectParticipantTimerValue(BaseModel):
    ParticipantTimerAction: Literal['Unset'] | None = None
    ParticipantTimerDurationInMinutes: StrictInt | None = None
