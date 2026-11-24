from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2MutualTlsAuthentication(BaseModel):
    TruststoreUri: StrictStr | None = None
    TruststoreVersion: StrictStr | None = None
    TruststoreWarnings: list[StrictStr] | None = None
