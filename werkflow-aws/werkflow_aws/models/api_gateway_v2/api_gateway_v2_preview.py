from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .api_gateway_v2_status_exception import APIGatewayV2StatusException


class APIGatewayV2Preview(BaseModel):
    PreviewStatus: StrictStr | None = None
    PreviewUrl: StrictStr | None = None
    StatusException: APIGatewayV2StatusException | None = None
