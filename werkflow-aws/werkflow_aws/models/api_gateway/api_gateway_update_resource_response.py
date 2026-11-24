from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_method import APIGatewayMethod


class APIGatewayUpdateResourceResponse(BaseModel):
    id: StrictStr | None = None
    parentId: StrictStr | None = None
    pathPart: StrictStr | None = None
    path: StrictStr | None = None
    resourceMethods: dict[StrictStr, APIGatewayMethod] | None = None
    ResponseMetadata: dict[str, Any] | None = None
