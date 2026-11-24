from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_front_key_value_store import CloudFrontKeyValueStore


class CloudFrontKeyValueStoreList(BaseModel):
    NextMarker: StrictStr | None = None
    MaxItems: StrictInt | None = None
    Quantity: StrictInt | None = None
    Items: list[CloudFrontKeyValueStore] | None = None
