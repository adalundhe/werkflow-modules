from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class ConnectParticipantConfiguration(BaseModel):
    ResponseMode: Literal['INCREMENTAL', 'COMPLETE'] | None = None
