from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2PlacementGroupInfo(BaseModel):
    SupportedStrategies: list[StrictStr] | None = None
