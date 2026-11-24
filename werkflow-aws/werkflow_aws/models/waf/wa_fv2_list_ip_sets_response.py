from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .wa_fv2_ip_set_summary import WAFv2IPSetSummary


class WAFv2ListIPSetsResponse(BaseModel):
    NextMarker: StrictStr | None = None
    IPSets: list[WAFv2IPSetSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
