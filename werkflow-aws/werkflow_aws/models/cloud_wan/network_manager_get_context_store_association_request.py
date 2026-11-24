from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerGetContextStoreAssociationRequest(BaseModel):
    ContextStoreId: StrictStr
    TransitGatewayArn: StrictStr
