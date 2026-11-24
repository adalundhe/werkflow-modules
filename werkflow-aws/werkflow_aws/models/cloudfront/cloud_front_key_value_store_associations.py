from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .cloud_front_key_value_store_association import CloudFrontKeyValueStoreAssociation


class CloudFrontKeyValueStoreAssociations(BaseModel):
    Quantity: StrictInt | None = None
    Items: list[CloudFrontKeyValueStoreAssociation] | None = None
