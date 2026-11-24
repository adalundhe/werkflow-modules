from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_endpoint_performance import SageMakerEndpointPerformance
from .sage_maker_inference_recommendation import SageMakerInferenceRecommendation
from .sage_maker_recommendation_job_input_config import SageMakerRecommendationJobInputConfig
from .sage_maker_recommendation_job_stopping_conditions import SageMakerRecommendationJobStoppingConditions


class SageMakerDescribeInferenceRecommendationsJobResponse(BaseModel):
    JobName: StrictStr | None = None
    JobDescription: StrictStr | None = None
    JobType: StrictStr | None = None
    JobArn: StrictStr | None = None
    RoleArn: StrictStr | None = None
    Status: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    CompletionTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    FailureReason: StrictStr | None = None
    InputConfig: SageMakerRecommendationJobInputConfig | None = None
    StoppingConditions: SageMakerRecommendationJobStoppingConditions | None = None
    InferenceRecommendations: list[SageMakerInferenceRecommendation] | None = None
    EndpointPerformances: list[SageMakerEndpointPerformance] | None = None
    ResponseMetadata: dict[str, Any] | None = None
