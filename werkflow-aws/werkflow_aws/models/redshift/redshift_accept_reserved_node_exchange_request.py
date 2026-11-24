from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftAcceptReservedNodeExchangeRequest(BaseModel):
    ReservedNodeId: StrictStr
    TargetReservedNodeOfferingId: StrictStr
