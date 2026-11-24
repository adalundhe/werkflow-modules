from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class APIGatewayCreateRequestValidatorRequest(BaseModel):
    restApiId: StrictStr
    name: StrictStr | None = None
    validateRequestBody: StrictBool | None = None
    validateRequestParameters: StrictBool | None = None
