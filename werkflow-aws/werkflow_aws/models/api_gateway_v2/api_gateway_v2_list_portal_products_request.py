from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2ListPortalProductsRequest(BaseModel):
    MaxResults: StrictStr | None = None
    NextToken: StrictStr | None = None
    ResourceOwner: StrictStr | None = None
