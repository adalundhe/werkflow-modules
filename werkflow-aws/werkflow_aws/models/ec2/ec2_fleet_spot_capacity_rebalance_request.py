from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt


class EC2FleetSpotCapacityRebalanceRequest(BaseModel):
    ReplacementStrategy: Literal['launch', 'launch-before-terminate'] | None = None
    TerminationDelay: StrictInt | None = None
