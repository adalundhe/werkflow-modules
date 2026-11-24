from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class EC2ProcessorInfo(BaseModel):
    SupportedArchitectures: list[StrictStr] | None = None
    SustainedClockSpeedInGhz: StrictFloat | StrictInt | None = None
    SupportedFeatures: list[StrictStr] | None = None
    Manufacturer: StrictStr | None = None
