from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESDisassociateEmailIdentityCertificateRequest(BaseModel):
    EmailIdentity: StrictStr
    FromAddress: StrictStr | None = None
