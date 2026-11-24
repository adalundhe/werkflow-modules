from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayDeleteClientCertificateRequest(BaseModel):
    clientCertificateId: StrictStr
