from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerWhenSentTo(BaseModel):
    WhenSentToSegmentsList: list[StrictStr] | None = None
