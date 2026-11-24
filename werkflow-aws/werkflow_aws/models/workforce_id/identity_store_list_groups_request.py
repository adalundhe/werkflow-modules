from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .identity_store_filter import IdentityStoreFilter


class IdentityStoreListGroupsRequest(BaseModel):
    IdentityStoreId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    Filters: list[IdentityStoreFilter] | None = None
