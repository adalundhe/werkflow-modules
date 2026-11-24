from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeDeviceFleetRequest(BaseModel):
    DeviceFleetName: StrictStr
