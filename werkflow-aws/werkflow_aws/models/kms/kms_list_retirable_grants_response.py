from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .kms_grant_list_entry import KMSGrantListEntry


class KMSListRetirableGrantsResponse(BaseModel):
    Grants: list[KMSGrantListEntry] | None = None
    NextMarker: StrictStr | None = None
    Truncated: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
