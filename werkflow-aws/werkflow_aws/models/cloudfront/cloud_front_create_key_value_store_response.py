from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_front_key_value_store import CloudFrontKeyValueStore


class CloudFrontCreateKeyValueStoreResponse(BaseModel):
    KeyValueStore: CloudFrontKeyValueStore | None = None
    ETag: StrictStr | None = None
    Location: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
