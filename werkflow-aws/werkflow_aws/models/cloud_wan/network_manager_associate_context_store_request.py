from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerAssociateContextStoreRequest(BaseModel):
    ContextStoreId: StrictStr
    TransitGatewayArn: StrictStr | None = None
