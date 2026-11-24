from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayGetClientCertificateRequest(BaseModel):
    clientCertificateId: StrictStr
