from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CloudFrontManagedCertificateRequest(BaseModel):
    ValidationTokenHost: Literal['cloudfront', 'self-hosted']
    PrimaryDomainName: StrictStr | None = None
    CertificateTransparencyLoggingPreference: Literal['enabled', 'disabled'] | None = None
