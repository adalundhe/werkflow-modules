from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESGetBlacklistReportsRequest(BaseModel):
    BlacklistItemNames: list[StrictStr]
