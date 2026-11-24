from __future__ import annotations
from pydantic import BaseModel
from .identity_store_external_id import IdentityStoreExternalId
from .identity_store_unique_attribute import IdentityStoreUniqueAttribute


class IdentityStoreAlternateIdentifier(BaseModel):
    ExternalId: IdentityStoreExternalId | None = None
    UniqueAttribute: IdentityStoreUniqueAttribute | None = None
