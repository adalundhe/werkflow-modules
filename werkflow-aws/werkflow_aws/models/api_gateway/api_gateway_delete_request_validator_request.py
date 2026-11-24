from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayDeleteRequestValidatorRequest(BaseModel):
    restApiId: StrictStr
    requestValidatorId: StrictStr
