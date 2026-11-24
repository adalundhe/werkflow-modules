from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EndUserMessagingPutKeywordRequest(BaseModel):
    OriginationIdentity: StrictStr
    Keyword: StrictStr
    KeywordMessage: StrictStr
    KeywordAction: Literal['AUTOMATIC_RESPONSE', 'OPT_OUT', 'OPT_IN'] | None = None
