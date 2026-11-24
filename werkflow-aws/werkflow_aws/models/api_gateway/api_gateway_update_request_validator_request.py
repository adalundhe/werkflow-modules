from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .api_gateway_patch_operation import APIGatewayPatchOperation


class APIGatewayUpdateRequestValidatorRequest(BaseModel):
    restApiId: StrictStr
    requestValidatorId: StrictStr
    patchOperations: list[APIGatewayPatchOperation] | None = None
