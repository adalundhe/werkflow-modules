from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class APIGatewayPutGatewayResponseResponse(BaseModel):
    responseType: StrictStr | None = None
    statusCode: StrictStr | None = None
    responseParameters: dict[StrictStr, StrictStr] | None = None
    responseTemplates: dict[StrictStr, StrictStr] | None = None
    defaultResponse: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
