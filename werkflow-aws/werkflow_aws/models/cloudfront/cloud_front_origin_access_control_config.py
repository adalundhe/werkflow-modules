from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontOriginAccessControlConfig(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    SigningProtocol: StrictStr | None = None
    SigningBehavior: StrictStr | None = None
    OriginAccessControlOriginType: StrictStr | None = None
