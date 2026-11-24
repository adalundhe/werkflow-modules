from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class APIGatewayUpdateMethodResponseResponse(BaseModel):
    statusCode: StrictStr | None = None
    responseParameters: dict[StrictStr, StrictBool] | None = None
    responseModels: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
