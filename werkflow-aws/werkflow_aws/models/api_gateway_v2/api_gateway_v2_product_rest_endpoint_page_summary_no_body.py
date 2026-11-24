from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .api_gateway_v2_rest_endpoint_identifier import APIGatewayV2RestEndpointIdentifier
from .api_gateway_v2_status_exception import APIGatewayV2StatusException


class APIGatewayV2ProductRestEndpointPageSummaryNoBody(BaseModel):
    Endpoint: StrictStr | None = None
    LastModified: datetime.datetime | StrictStr | None = None
    OperationName: StrictStr | None = None
    ProductRestEndpointPageArn: StrictStr | None = None
    ProductRestEndpointPageId: StrictStr | None = None
    RestEndpointIdentifier: APIGatewayV2RestEndpointIdentifier | None = None
    Status: StrictStr | None = None
    StatusException: APIGatewayV2StatusException | None = None
    TryItState: StrictStr | None = None
