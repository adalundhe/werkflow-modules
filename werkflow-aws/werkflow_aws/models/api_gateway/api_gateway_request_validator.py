from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class APIGatewayRequestValidator(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    validateRequestBody: StrictBool | None = None
    validateRequestParameters: StrictBool | None = None
