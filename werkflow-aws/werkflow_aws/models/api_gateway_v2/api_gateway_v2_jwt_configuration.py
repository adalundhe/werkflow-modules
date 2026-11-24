from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2JWTConfiguration(BaseModel):
    Audience: list[StrictStr] | None = None
    Issuer: StrictStr | None = None
