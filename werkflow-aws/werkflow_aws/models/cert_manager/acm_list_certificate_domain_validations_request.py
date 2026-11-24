from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ACMListCertificateDomainValidationsRequest(BaseModel):
    CertificateArn: StrictStr
    NextToken: StrictStr | None = None
    MaxItems: StrictInt | None = None
