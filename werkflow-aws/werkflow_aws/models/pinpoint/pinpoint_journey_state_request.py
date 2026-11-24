from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class PinpointJourneyStateRequest(BaseModel):
    State: Literal['DRAFT', 'ACTIVE', 'COMPLETED', 'CANCELLED', 'CLOSED', 'PAUSED'] | None = None
