from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .api_gateway_method import APIGatewayMethod


class APIGatewayResource(BaseModel):
    id: StrictStr | None = None
    parentId: StrictStr | None = None
    pathPart: StrictStr | None = None
    path: StrictStr | None = None
    resourceMethods: dict[StrictStr, APIGatewayMethod] | None = None
