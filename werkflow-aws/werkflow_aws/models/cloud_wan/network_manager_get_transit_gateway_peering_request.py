from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerGetTransitGatewayPeeringRequest(BaseModel):
    PeeringId: StrictStr
