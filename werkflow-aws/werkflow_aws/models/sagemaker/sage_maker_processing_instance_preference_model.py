from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerProcessingInstancePreferenceModel(BaseModel):
    InstanceType: StrictStr | None = None
    InstanceCount: StrictInt | None = None
