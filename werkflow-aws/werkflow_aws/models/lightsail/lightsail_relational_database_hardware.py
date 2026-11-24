from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class LightsailRelationalDatabaseHardware(BaseModel):
    cpuCount: StrictInt | None = None
    diskSizeInGb: StrictInt | None = None
    ramSizeInGb: StrictFloat | StrictInt | None = None
