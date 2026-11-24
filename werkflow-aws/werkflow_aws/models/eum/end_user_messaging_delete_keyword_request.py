from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingDeleteKeywordRequest(BaseModel):
    OriginationIdentity: StrictStr
    Keyword: StrictStr
