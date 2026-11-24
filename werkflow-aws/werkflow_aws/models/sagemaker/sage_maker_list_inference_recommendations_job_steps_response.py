from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_inference_recommendations_job_step import SageMakerInferenceRecommendationsJobStep


class SageMakerListInferenceRecommendationsJobStepsResponse(BaseModel):
    Steps: list[SageMakerInferenceRecommendationsJobStep] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
