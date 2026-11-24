from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictFloat, StrictInt


class XRaySamplingStrategy(BaseModel):
    Name: Literal['PartialScan', 'FixedRate'] | None = None
    Value: StrictFloat | StrictInt | None = None
