from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .end_user_messaging_pool_origination_identities_filter import EndUserMessagingPoolOriginationIdentitiesFilter


class EndUserMessagingListPoolOriginationIdentitiesRequest(BaseModel):
    PoolId: StrictStr
    Filters: list[EndUserMessagingPoolOriginationIdentitiesFilter] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
