from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerInferenceComponentPlacementStatus(BaseModel):
    InstanceType: StrictStr | None = None
    CurrentCopyCount: StrictInt | None = None
