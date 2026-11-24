from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .end_user_messaging_keyword_filter import EndUserMessagingKeywordFilter


class EndUserMessagingDescribeKeywordsRequest(BaseModel):
    OriginationIdentity: StrictStr
    Keywords: list[StrictStr] | None = None
    Filters: list[EndUserMessagingKeywordFilter] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
