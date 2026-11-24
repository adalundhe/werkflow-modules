from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IdentityStoreListIdentityStoresRequest(BaseModel):
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
