from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_device import SageMakerDevice


class SageMakerUpdateDevicesRequest(BaseModel):
    DeviceFleetName: StrictStr
    Devices: list[SageMakerDevice]
