from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .acm_certificate_authority import ACMCertificateAuthority


class ACMUpdateAcmeEndpointRequest(BaseModel):
    AcmeEndpointArn: StrictStr
    AuthorizationBehavior: Literal['PRE_APPROVED'] | None = None
    Contact: Literal['REQUIRED', 'NOT_REQUIRED'] | None = None
    CertificateAuthority: ACMCertificateAuthority | None = None
