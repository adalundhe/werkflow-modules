from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class FMSGetProtocolsListRequest(BaseModel):
    ListId: StrictStr
    DefaultList: StrictBool | None = None
