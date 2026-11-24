from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class EndUserMessagingPutKeywordResponse(BaseModel):
    OriginationIdentityArn: StrictStr | None = None
    OriginationIdentity: StrictStr | None = None
    Keyword: StrictStr | None = None
    KeywordMessage: StrictStr | None = None
    KeywordAction: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
