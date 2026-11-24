from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .api_gateway_documentation_part_location import APIGatewayDocumentationPartLocation


class APIGatewayCreateDocumentationPartRequest(BaseModel):
    restApiId: StrictStr
    location: APIGatewayDocumentationPartLocation
    properties: StrictStr
