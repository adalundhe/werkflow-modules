from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerDeletePeeringRequest(BaseModel):
    PeeringId: StrictStr
