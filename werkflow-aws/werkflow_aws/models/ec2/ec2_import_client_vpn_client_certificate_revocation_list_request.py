from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ImportClientVpnClientCertificateRevocationListRequest(BaseModel):
    ClientVpnEndpointId: StrictStr
    CertificateRevocationList: StrictStr
    DryRun: StrictBool | None = None
