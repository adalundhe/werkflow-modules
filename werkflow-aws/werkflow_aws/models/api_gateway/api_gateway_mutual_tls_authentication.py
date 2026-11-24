from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayMutualTlsAuthentication(BaseModel):
    truststoreUri: StrictStr | None = None
    truststoreVersion: StrictStr | None = None
    truststoreWarnings: list[StrictStr] | None = None
