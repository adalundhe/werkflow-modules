from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_documentation_part_location import APIGatewayDocumentationPartLocation


class APIGatewayUpdateDocumentationPartResponse(BaseModel):
    id: StrictStr | None = None
    location: APIGatewayDocumentationPartLocation | None = None
    properties: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
