from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeInferenceRecommendationsJobRequest(BaseModel):
    JobName: StrictStr
