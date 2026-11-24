from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2CertificateAuthentication(BaseModel):
    ClientRootCertificateChain: StrictStr | None = None
