from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2GetProductRestEndpointPageRequest(BaseModel):
    PortalProductId: StrictStr
    ProductRestEndpointPageId: StrictStr
    IncludeRawDisplayContent: StrictStr | None = None
    ResourceOwnerAccountId: StrictStr | None = None
