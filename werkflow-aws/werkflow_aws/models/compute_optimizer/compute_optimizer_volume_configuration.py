from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class ComputeOptimizerVolumeConfiguration(BaseModel):
    volumeType: StrictStr | None = None
    volumeSize: StrictInt | None = None
    volumeBaselineIOPS: StrictInt | None = None
    volumeBurstIOPS: StrictInt | None = None
    volumeBaselineThroughput: StrictInt | None = None
    volumeBurstThroughput: StrictInt | None = None
    rootVolume: StrictBool | None = None
