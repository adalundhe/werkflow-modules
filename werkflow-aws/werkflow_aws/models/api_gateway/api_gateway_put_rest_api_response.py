from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .api_gateway_endpoint_configuration import APIGatewayEndpointConfiguration


class APIGatewayPutRestApiResponse(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    createdDate: datetime.datetime | StrictStr | None = None
    version: StrictStr | None = None
    warnings: list[StrictStr] | None = None
    binaryMediaTypes: list[StrictStr] | None = None
    minimumCompressionSize: StrictInt | None = None
    apiKeySource: StrictStr | None = None
    endpointConfiguration: APIGatewayEndpointConfiguration | None = None
    policy: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    disableExecuteApiEndpoint: StrictBool | None = None
    rootResourceId: StrictStr | None = None
    securityPolicy: StrictStr | None = None
    endpointAccessMode: StrictStr | None = None
    apiStatus: StrictStr | None = None
    apiStatusMessage: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
