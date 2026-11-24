from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_documentation_version import APIGatewayDocumentationVersion


class APIGatewayGetDocumentationVersionsResponse(BaseModel):
    position: StrictStr | None = None
    items: list[APIGatewayDocumentationVersion] | None = None
    ResponseMetadata: dict[str, Any] | None = None
