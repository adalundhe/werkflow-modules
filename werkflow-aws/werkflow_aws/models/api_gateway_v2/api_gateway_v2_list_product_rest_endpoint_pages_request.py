from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2ListProductRestEndpointPagesRequest(BaseModel):
    PortalProductId: StrictStr
    MaxResults: StrictStr | None = None
    NextToken: StrictStr | None = None
    ResourceOwnerAccountId: StrictStr | None = None
