from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2FleetSpotCapacityRebalance(BaseModel):
    ReplacementStrategy: StrictStr | None = None
    TerminationDelay: StrictInt | None = None
