from __future__ import annotations
from pydantic import BaseModel
from .connect_participant_capabilities import ConnectParticipantCapabilities


class ConnectAllowedCapabilities(BaseModel):
    Customer: ConnectParticipantCapabilities | None = None
    Agent: ConnectParticipantCapabilities | None = None
