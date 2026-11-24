from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field
from .api_gateway_v2_display_content_overrides import APIGatewayV2DisplayContentOverrides
from .api_gateway_v2_none import APIGatewayV2None


class APIGatewayV2EndpointDisplayContent(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    None_: APIGatewayV2None | None = Field(default=None, alias='None')
    Overrides: APIGatewayV2DisplayContentOverrides | None = None
