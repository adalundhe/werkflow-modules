from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_participant_token_credentials import ConnectParticipantTokenCredentials


class ConnectCreateParticipantResponse(BaseModel):
    ParticipantCredentials: ConnectParticipantTokenCredentials | None = None
    ParticipantId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
