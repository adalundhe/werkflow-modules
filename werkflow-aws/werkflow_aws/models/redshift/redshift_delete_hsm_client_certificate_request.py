from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftDeleteHsmClientCertificateRequest(BaseModel):
    HsmClientCertificateIdentifier: StrictStr
