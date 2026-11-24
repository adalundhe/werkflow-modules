from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2GetIntegrationResponsesRequest(BaseModel):
    ApiId: StrictStr
    IntegrationId: StrictStr
    MaxResults: StrictStr | None = None
    NextToken: StrictStr | None = None
