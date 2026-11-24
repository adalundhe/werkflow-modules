from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .wa_fv2_web_acl import WAFv2WebACL


class WAFv2GetWebACLResponse(BaseModel):
    WebACL: WAFv2WebACL | None = None
    LockToken: StrictStr | None = None
    ApplicationIntegrationURL: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
