from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerStopInferenceRecommendationsJobRequest(BaseModel):
    JobName: StrictStr
