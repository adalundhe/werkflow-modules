from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .api_gateway_patch_operation import APIGatewayPatchOperation


class APIGatewayUpdateDeploymentRequest(BaseModel):
    restApiId: StrictStr
    deploymentId: StrictStr
    patchOperations: list[APIGatewayPatchOperation] | None = None
