from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .api_gateway_documentation_part_location import APIGatewayDocumentationPartLocation


class APIGatewayDocumentationPart(BaseModel):
    id: StrictStr | None = None
    location: APIGatewayDocumentationPartLocation | None = None
    properties: StrictStr | None = None
