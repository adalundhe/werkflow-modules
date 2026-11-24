from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerDeviceSelectionConfig(BaseModel):
    DeviceSubsetType: StrictStr | None = None
    Percentage: StrictInt | None = None
    DeviceNames: list[StrictStr] | None = None
    DeviceNameContains: StrictStr | None = None
