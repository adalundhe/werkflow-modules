from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_documentation_part import APIGatewayDocumentationPart


class APIGatewayGetDocumentationPartsResponse(BaseModel):
    position: StrictStr | None = None
    items: list[APIGatewayDocumentationPart] | None = None
    ResponseMetadata: dict[str, Any] | None = None
