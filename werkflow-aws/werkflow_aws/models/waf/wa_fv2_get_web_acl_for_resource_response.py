from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .wa_fv2_web_acl import WAFv2WebACL


class WAFv2GetWebACLForResourceResponse(BaseModel):
    WebACL: WAFv2WebACL | None = None
    ResponseMetadata: dict[str, Any] | None = None
