from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .api_gateway_patch_operation import APIGatewayPatchOperation


class APIGatewayUpdateBasePathMappingRequest(BaseModel):
    domainName: StrictStr
    basePath: StrictStr
    domainNameId: StrictStr | None = None
    patchOperations: list[APIGatewayPatchOperation] | None = None
