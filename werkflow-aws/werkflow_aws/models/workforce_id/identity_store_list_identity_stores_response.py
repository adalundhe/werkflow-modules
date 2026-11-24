from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .identity_store import IdentityStore


class IdentityStoreListIdentityStoresResponse(BaseModel):
    IdentityStores: list[IdentityStore] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
