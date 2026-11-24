from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .identity_store_alternate_identifier import IdentityStoreAlternateIdentifier


class IdentityStoreGetUserIdRequest(BaseModel):
    IdentityStoreId: StrictStr
    AlternateIdentifier: IdentityStoreAlternateIdentifier
