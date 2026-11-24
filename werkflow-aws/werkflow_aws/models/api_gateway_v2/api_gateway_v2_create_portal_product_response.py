from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_v2_display_order import APIGatewayV2DisplayOrder


class APIGatewayV2CreatePortalProductResponse(BaseModel):
    Description: StrictStr | None = None
    DisplayName: StrictStr | None = None
    DisplayOrder: APIGatewayV2DisplayOrder | None = None
    LastModified: datetime.datetime | StrictStr | None = None
    PortalProductArn: StrictStr | None = None
    PortalProductId: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
