from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .api_gateway_v2_custom_colors import APIGatewayV2CustomColors


class APIGatewayV2PortalTheme(BaseModel):
    CustomColors: APIGatewayV2CustomColors | None = None
    LogoLastUploaded: datetime.datetime | StrictStr | None = None
