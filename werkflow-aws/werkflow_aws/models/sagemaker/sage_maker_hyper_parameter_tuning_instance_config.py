from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerHyperParameterTuningInstanceConfig(BaseModel):
    InstanceType: StrictStr | None = None
    InstanceCount: StrictInt | None = None
    VolumeSizeInGB: StrictInt | None = None
