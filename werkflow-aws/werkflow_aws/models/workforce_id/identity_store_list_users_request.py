from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .identity_store_filter import IdentityStoreFilter


class IdentityStoreListUsersRequest(BaseModel):
    IdentityStoreId: StrictStr
    Extensions: list[StrictStr] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    Filters: list[IdentityStoreFilter] | None = None
