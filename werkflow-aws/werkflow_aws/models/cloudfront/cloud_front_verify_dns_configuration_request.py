from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontVerifyDnsConfigurationRequest(BaseModel):
    Identifier: StrictStr
    Domain: StrictStr | None = None
