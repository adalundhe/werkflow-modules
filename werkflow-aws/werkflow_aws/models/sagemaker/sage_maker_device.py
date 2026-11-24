from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDevice(BaseModel):
    DeviceName: StrictStr
    Description: StrictStr | None = None
    IotThingName: StrictStr | None = None
