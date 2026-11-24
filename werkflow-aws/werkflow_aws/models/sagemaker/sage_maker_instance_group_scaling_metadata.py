from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerInstanceGroupScalingMetadata(BaseModel):
    InstanceCount: StrictInt | None = None
    TargetCount: StrictInt | None = None
    MinCount: StrictInt | None = None
    FailureMessage: StrictStr | None = None
