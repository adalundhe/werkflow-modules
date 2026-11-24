from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .acm_certificate_authority import ACMCertificateAuthority
from .acm_tag import ACMTag


class AcmeEndpointSummary(BaseModel):
    AcmeEndpointArn: StrictStr | None = None
    EndpointUrl: StrictStr | None = None
    Status: StrictStr | None = None
    FailureReason: StrictStr | None = None
    AuthorizationBehavior: StrictStr | None = None
    Contact: StrictStr | None = None
    CertificateAuthority: ACMCertificateAuthority | None = None
    CertificateTags: list[ACMTag] | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
