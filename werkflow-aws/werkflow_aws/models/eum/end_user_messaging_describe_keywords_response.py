from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .end_user_messaging_keyword_information import EndUserMessagingKeywordInformation


class EndUserMessagingDescribeKeywordsResponse(BaseModel):
    OriginationIdentityArn: StrictStr | None = None
    OriginationIdentity: StrictStr | None = None
    Keywords: list[EndUserMessagingKeywordInformation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
