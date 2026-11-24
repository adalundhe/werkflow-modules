from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .wa_fv2_ip_set_summary import WAFv2IPSetSummary


class WAFv2CreateIPSetResponse(BaseModel):
    Summary: WAFv2IPSetSummary | None = None
    ResponseMetadata: dict[str, Any] | None = None
