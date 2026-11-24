from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .wa_fv2_web_acl_summary import WAFv2WebACLSummary


class WAFv2CreateWebACLResponse(BaseModel):
    Summary: WAFv2WebACLSummary | None = None
    ResponseMetadata: dict[str, Any] | None = None
