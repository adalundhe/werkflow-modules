from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class APIGatewayCreateRequestValidatorResponse(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    validateRequestBody: StrictBool | None = None
    validateRequestParameters: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
