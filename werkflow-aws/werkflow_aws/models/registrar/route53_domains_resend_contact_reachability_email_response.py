from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class Route53DomainsResendContactReachabilityEmailResponse(BaseModel):
    domainName: StrictStr | None = None
    emailAddress: StrictStr | None = None
    isAlreadyVerified: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
