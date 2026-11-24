from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .api_gateway_patch_operation import APIGatewayPatchOperation


class APIGatewayUpdateAuthorizerRequest(BaseModel):
    restApiId: StrictStr
    authorizerId: StrictStr
    patchOperations: list[APIGatewayPatchOperation] | None = None
