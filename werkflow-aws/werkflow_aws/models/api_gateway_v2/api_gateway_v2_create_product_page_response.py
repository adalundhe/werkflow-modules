from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_v2_display_content import APIGatewayV2DisplayContent


class APIGatewayV2CreateProductPageResponse(BaseModel):
    DisplayContent: APIGatewayV2DisplayContent | None = None
    LastModified: datetime.datetime | StrictStr | None = None
    ProductPageArn: StrictStr | None = None
    ProductPageId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
