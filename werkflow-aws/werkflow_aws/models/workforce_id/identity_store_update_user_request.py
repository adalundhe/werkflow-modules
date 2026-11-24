from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .identity_store_attribute_operation import IdentityStoreAttributeOperation


class IdentityStoreUpdateUserRequest(BaseModel):
    IdentityStoreId: StrictStr
    UserId: StrictStr
    Operations: list[IdentityStoreAttributeOperation]
    Revision: StrictStr | None = None
