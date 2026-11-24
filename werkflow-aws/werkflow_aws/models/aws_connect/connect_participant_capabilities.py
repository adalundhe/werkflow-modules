from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectParticipantCapabilities(BaseModel):
    Video: StrictStr | None = None
    ScreenShare: StrictStr | None = None
