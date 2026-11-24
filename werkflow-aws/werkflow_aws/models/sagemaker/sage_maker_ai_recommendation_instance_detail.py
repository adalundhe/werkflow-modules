from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerAIRecommendationInstanceDetail(BaseModel):
    InstanceType: StrictStr | None = None
    InstanceCount: StrictInt | None = None
    CopyCountPerInstance: StrictInt | None = None
