from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerMonitoringClusterConfig(BaseModel):
    InstanceCount: StrictInt | None = None
    InstanceType: StrictStr | None = None
    VolumeSizeInGB: StrictInt | None = None
    VolumeKmsKeyId: StrictStr | None = None
