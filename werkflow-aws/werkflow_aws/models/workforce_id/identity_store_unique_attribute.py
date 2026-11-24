from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .identity_store_attribute_value import IdentityStoreAttributeValue


class IdentityStoreUniqueAttribute(BaseModel):
    AttributePath: StrictStr
    AttributeValue: IdentityStoreAttributeValue
