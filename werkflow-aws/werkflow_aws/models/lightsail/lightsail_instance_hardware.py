from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .lightsail_disk import LightsailDisk


class LightsailInstanceHardware(BaseModel):
    cpuCount: StrictInt | None = None
    disks: list[LightsailDisk] | None = None
    ramSizeInGb: StrictFloat | StrictInt | None = None
