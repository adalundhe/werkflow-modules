from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .api_gateway_v2_portal_theme import APIGatewayV2PortalTheme


class APIGatewayV2PortalContent(BaseModel):
    Description: StrictStr | None = None
    DisplayName: StrictStr | None = None
    Theme: APIGatewayV2PortalTheme | None = None
