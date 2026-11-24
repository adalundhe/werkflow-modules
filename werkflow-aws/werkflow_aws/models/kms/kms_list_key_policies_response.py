from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class KMSListKeyPoliciesResponse(BaseModel):
    PolicyNames: list[StrictStr] | None = None
    NextMarker: StrictStr | None = None
    Truncated: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
