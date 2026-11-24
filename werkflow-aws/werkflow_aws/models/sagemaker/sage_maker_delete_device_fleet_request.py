from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteDeviceFleetRequest(BaseModel):
    DeviceFleetName: StrictStr
