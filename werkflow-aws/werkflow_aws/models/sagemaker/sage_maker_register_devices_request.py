from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_device import SageMakerDevice
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerRegisterDevicesRequest(BaseModel):
    DeviceFleetName: StrictStr
    Devices: list[SageMakerDevice]
    Tags: list[SageMakerTagModel] | None = None
