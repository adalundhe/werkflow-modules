from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class IAMGetOutboundWebIdentityFederationInfoResponse(BaseModel):
    IssuerIdentifier: StrictStr | None = None
    JwtVendingEnabled: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
