from __future__ import annotations
from pydantic import BaseModel, StrictInt


class ConnectRealTimeContactAnalysisCharacterInterval(BaseModel):
    BeginOffsetChar: StrictInt | None = None
    EndOffsetChar: StrictInt | None = None
