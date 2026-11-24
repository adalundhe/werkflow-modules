from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2MutualTlsAuthenticationInput(BaseModel):
    TruststoreUri: StrictStr | None = None
    TruststoreVersion: StrictStr | None = None
