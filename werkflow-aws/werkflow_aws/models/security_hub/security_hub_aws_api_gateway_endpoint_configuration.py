from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsApiGatewayEndpointConfiguration(BaseModel):
    Types: list[StrictStr] | None = None
