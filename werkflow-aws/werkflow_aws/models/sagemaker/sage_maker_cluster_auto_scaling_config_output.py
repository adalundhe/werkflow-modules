from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerClusterAutoScalingConfigOutput(BaseModel):
    Mode: StrictStr | None = None
    AutoScalerType: StrictStr | None = None
    Status: StrictStr | None = None
    FailureMessage: StrictStr | None = None
