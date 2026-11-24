from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .end_user_messaging_opted_out_filter import EndUserMessagingOptedOutFilter


class EndUserMessagingDescribeOptedOutNumbersRequest(BaseModel):
    OptOutListName: StrictStr
    OptedOutNumbers: list[StrictStr] | None = None
    Filters: list[EndUserMessagingOptedOutFilter] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
