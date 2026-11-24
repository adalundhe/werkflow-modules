from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListInferenceRecommendationsJobStepsRequest(BaseModel):
    JobName: StrictStr
    Status: Literal['PENDING', 'IN_PROGRESS', 'COMPLETED', 'FAILED', 'STOPPING', 'STOPPED', 'DELETING', 'DELETED'] | None = None
    StepType: Literal['BENCHMARK'] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
