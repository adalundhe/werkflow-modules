from __future__ import annotations
from pydantic import BaseModel, StrictBool


class APIGatewayV2ParameterConstraints(BaseModel):
    Required: StrictBool | None = None
