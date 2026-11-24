from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .kms_rotations_list_entry import KMSRotationsListEntry


class KMSListKeyRotationsResponse(BaseModel):
    Rotations: list[KMSRotationsListEntry] | None = None
    NextMarker: StrictStr | None = None
    Truncated: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
