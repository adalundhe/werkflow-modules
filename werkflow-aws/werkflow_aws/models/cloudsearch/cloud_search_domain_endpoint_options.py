from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudSearchDomainEndpointOptions(BaseModel):
    EnforceHTTPS: StrictBool | None = None
    TLSSecurityPolicy: StrictStr | None = None
