from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class IAMListUserPoliciesResponse(BaseModel):
    PolicyNames: list[StrictStr] | None = None
    IsTruncated: StrictBool | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
