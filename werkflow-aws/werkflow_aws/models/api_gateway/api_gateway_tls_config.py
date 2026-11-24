from __future__ import annotations
from pydantic import BaseModel, StrictBool


class APIGatewayTlsConfig(BaseModel):
    insecureSkipVerification: StrictBool | None = None
