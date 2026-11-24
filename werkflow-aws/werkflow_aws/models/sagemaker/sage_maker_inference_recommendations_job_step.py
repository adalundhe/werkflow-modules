from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_recommendation_job_inference_benchmark import SageMakerRecommendationJobInferenceBenchmark


class SageMakerInferenceRecommendationsJobStep(BaseModel):
    StepType: StrictStr | None = None
    JobName: StrictStr | None = None
    Status: StrictStr | None = None
    InferenceBenchmark: SageMakerRecommendationJobInferenceBenchmark | None = None
