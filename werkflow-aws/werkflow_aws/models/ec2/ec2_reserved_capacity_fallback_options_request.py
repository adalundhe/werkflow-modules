from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class EC2ReservedCapacityFallbackOptionsRequest(BaseModel):
    MarketTypes: list[Literal['on-demand']] | None = None
