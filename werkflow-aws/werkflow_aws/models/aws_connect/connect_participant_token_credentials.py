from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectParticipantTokenCredentials(BaseModel):
    ParticipantToken: StrictStr | None = None
    Expiry: StrictStr | None = None
