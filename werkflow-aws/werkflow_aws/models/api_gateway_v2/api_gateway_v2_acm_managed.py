from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2ACMManaged(BaseModel):
    CertificateArn: StrictStr
    DomainName: StrictStr
