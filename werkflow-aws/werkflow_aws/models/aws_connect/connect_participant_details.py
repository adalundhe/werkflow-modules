from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectParticipantDetails(BaseModel):
    DisplayName: StrictStr
