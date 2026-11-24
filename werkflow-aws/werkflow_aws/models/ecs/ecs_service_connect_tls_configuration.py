from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_service_connect_tls_certificate_authority import ECSServiceConnectTlsCertificateAuthority


class ECSServiceConnectTlsConfiguration(BaseModel):
    issuerCertificateAuthority: ECSServiceConnectTlsCertificateAuthority | None = None
    kmsKey: StrictStr | None = None
    roleArn: StrictStr | None = None
