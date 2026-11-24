from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .kms_key_list_entry import KMSKeyListEntry


class KMSListKeysResponse(BaseModel):
    Keys: list[KMSKeyListEntry] | None = None
    NextMarker: StrictStr | None = None
    Truncated: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
