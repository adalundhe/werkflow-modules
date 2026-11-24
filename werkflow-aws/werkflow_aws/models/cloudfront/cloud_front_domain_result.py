from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontDomainResult(BaseModel):
    Domain: StrictStr | None = None
    Status: StrictStr | None = None
    ServeOn: StrictStr | None = None
