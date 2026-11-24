from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ACMResendValidationEmailRequest(BaseModel):
    CertificateArn: StrictStr
    Domain: StrictStr
    ValidationDomain: StrictStr
