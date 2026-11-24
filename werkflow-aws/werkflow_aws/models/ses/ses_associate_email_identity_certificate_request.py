from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESAssociateEmailIdentityCertificateRequest(BaseModel):
    EmailIdentity: StrictStr
    CertificateArn: StrictStr
    FromAddress: StrictStr | None = None
