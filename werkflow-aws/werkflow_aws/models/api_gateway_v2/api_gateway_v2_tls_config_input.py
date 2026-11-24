from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2TlsConfigInput(BaseModel):
    ServerNameToVerify: StrictStr | None = None
