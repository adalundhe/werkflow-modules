from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectContactLensChannelConfiguration(BaseModel):
    AnalyticsModes: list[StrictStr] | None = None
