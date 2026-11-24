from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSDeleteProtocolsListRequest(BaseModel):
    ListId: StrictStr
