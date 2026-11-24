from __future__ import annotations
from pydantic import BaseModel
from .api_gateway_patch_operation import APIGatewayPatchOperation


class APIGatewayUpdateAccountRequest(BaseModel):
    patchOperations: list[APIGatewayPatchOperation] | None = None
