from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPCustomDomainConfigType(BaseModel):
    CertificateArn: StrictStr | None = None
    SecurityPolicy: StrictStr | None = None
