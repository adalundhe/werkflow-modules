from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerServiceInsertionSegments(BaseModel):
    SendVia: list[StrictStr] | None = None
    SendTo: list[StrictStr] | None = None
