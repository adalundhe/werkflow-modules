from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .api_gateway_v2_cors import APIGatewayV2Cors


class APIGatewayV2GetApiResponse(BaseModel):
    ApiEndpoint: StrictStr | None = None
    ApiGatewayManaged: StrictBool | None = None
    ApiId: StrictStr | None = None
    ApiKeySelectionExpression: StrictStr | None = None
    CorsConfiguration: APIGatewayV2Cors | None = None
    CreatedDate: datetime.datetime | StrictStr | None = None
    Description: StrictStr | None = None
    DisableSchemaValidation: StrictBool | None = None
    DisableExecuteApiEndpoint: StrictBool | None = None
    ImportInfo: list[StrictStr] | None = None
    IpAddressType: StrictStr | None = None
    Name: StrictStr | None = None
    ProtocolType: StrictStr | None = None
    RouteSelectionExpression: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    Version: StrictStr | None = None
    Warnings: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
