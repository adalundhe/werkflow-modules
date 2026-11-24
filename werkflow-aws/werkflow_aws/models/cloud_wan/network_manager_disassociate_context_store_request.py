from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerDisassociateContextStoreRequest(BaseModel):
    ContextStoreId: StrictStr
    TransitGatewayArn: StrictStr
