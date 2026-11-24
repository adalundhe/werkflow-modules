from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2DeleteDomainNameRequest(BaseModel):
    DomainName: StrictStr
