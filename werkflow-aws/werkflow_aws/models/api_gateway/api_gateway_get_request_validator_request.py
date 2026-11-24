from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayGetRequestValidatorRequest(BaseModel):
    restApiId: StrictStr
    requestValidatorId: StrictStr
