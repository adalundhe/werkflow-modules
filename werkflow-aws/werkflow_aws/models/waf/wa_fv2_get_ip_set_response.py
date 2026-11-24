from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .wa_fv2_ip_set import WAFv2IPSet


class WAFv2GetIPSetResponse(BaseModel):
    IPSet: WAFv2IPSet | None = None
    LockToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
