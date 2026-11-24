from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTMachineLearningDetectionConfig(BaseModel):
    confidenceLevel: StrictStr | None = None
