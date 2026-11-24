from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingKeywordInformation(BaseModel):
    Keyword: StrictStr | None = None
    KeywordMessage: StrictStr | None = None
    KeywordAction: StrictStr | None = None
