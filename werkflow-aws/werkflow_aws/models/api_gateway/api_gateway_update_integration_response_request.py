from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .api_gateway_patch_operation import APIGatewayPatchOperation


class APIGatewayUpdateIntegrationResponseRequest(BaseModel):
    restApiId: StrictStr
    resourceId: StrictStr
    httpMethod: StrictStr
    statusCode: StrictStr
    patchOperations: list[APIGatewayPatchOperation] | None = None
