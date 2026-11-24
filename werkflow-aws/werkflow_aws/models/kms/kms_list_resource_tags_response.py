from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .kms_tag import KMSTag


class KMSListResourceTagsResponse(BaseModel):
    Tags: list[KMSTag] | None = None
    NextMarker: StrictStr | None = None
    Truncated: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
