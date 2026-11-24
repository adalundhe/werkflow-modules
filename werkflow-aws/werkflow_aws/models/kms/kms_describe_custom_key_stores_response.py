from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .kms_custom_key_stores_list_entry import KMSCustomKeyStoresListEntry


class KMSDescribeCustomKeyStoresResponse(BaseModel):
    CustomKeyStores: list[KMSCustomKeyStoresListEntry] | None = None
    NextMarker: StrictStr | None = None
    Truncated: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
