from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class LightsailInstanceEntry(BaseModel):
    sourceName: StrictStr
    instanceType: StrictStr
    portInfoSource: Literal['DEFAULT', 'INSTANCE', 'NONE', 'CLOSED']
    availabilityZone: StrictStr
    userData: StrictStr | None = None
