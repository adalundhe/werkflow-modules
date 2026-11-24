from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerEdgeModelStat(BaseModel):
    ModelName: StrictStr | None = None
    ModelVersion: StrictStr | None = None
    OfflineDeviceCount: StrictInt | None = None
    ConnectedDeviceCount: StrictInt | None = None
    ActiveDeviceCount: StrictInt | None = None
    SamplingDeviceCount: StrictInt | None = None
