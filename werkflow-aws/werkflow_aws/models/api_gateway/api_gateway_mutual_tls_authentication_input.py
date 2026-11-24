from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayMutualTlsAuthenticationInput(BaseModel):
    truststoreUri: StrictStr | None = None
    truststoreVersion: StrictStr | None = None
