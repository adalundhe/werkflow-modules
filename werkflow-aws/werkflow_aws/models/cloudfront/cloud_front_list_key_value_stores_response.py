from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_front_key_value_store_list import CloudFrontKeyValueStoreList


class CloudFrontListKeyValueStoresResponse(BaseModel):
    KeyValueStoreList: CloudFrontKeyValueStoreList | None = None
    ResponseMetadata: dict[str, Any] | None = None
