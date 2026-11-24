from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2EndpointDisplayContentResponse(BaseModel):
    Body: StrictStr | None = None
    Endpoint: StrictStr | None = None
    OperationName: StrictStr | None = None
