from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .acm_certificate_authority import ACMCertificateAuthority
from .acm_tag import ACMTag


class ACMCreateAcmeEndpointRequest(BaseModel):
    AuthorizationBehavior: Literal['PRE_APPROVED']
    CertificateAuthority: ACMCertificateAuthority
    IdempotencyToken: StrictStr | None = None
    Contact: Literal['REQUIRED', 'NOT_REQUIRED'] | None = None
    Tags: list[ACMTag] | None = None
    CertificateTags: list[ACMTag] | None = None
