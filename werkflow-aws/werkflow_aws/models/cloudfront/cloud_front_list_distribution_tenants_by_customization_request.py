from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudFrontListDistributionTenantsByCustomizationRequest(BaseModel):
    WebACLArn: StrictStr | None = None
    CertificateArn: StrictStr | None = None
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
