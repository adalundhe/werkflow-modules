from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeregisterDevicesRequest(BaseModel):
    DeviceFleetName: StrictStr
    DeviceNames: list[StrictStr]
