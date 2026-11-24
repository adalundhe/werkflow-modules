from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2CertificateAuthenticationRequest(BaseModel):
    ClientRootCertificateChainArn: StrictStr | None = None
