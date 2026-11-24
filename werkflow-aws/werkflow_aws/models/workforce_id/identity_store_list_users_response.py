from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .identity_store_user import IdentityStoreUser


class IdentityStoreListUsersResponse(BaseModel):
    Users: list[IdentityStoreUser] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
