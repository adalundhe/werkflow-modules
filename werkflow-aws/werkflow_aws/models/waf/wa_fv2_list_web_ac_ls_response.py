from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .wa_fv2_web_acl_summary import WAFv2WebACLSummary


class WAFv2ListWebACLsResponse(BaseModel):
    NextMarker: StrictStr | None = None
    WebACLs: list[WAFv2WebACLSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
