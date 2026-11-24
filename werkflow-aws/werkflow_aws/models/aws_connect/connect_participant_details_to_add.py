from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .connect_participant_capabilities import ConnectParticipantCapabilities


class ConnectParticipantDetailsToAdd(BaseModel):
    ParticipantRole: Literal['AGENT', 'CUSTOMER', 'SYSTEM', 'CUSTOM_BOT', 'SUPERVISOR'] | None = None
    DisplayName: StrictStr | None = None
    ParticipantCapabilities: ConnectParticipantCapabilities | None = None
