from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeDeviceRequest(BaseModel):
    DeviceName: StrictStr
    DeviceFleetName: StrictStr
    NextToken: StrictStr | None = None
