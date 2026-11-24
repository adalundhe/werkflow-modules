from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .sage_maker_recommendation_job_input_config import SageMakerRecommendationJobInputConfig
from .sage_maker_recommendation_job_output_config import SageMakerRecommendationJobOutputConfig
from .sage_maker_recommendation_job_stopping_conditions import SageMakerRecommendationJobStoppingConditions
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateInferenceRecommendationsJobRequest(BaseModel):
    JobName: StrictStr
    JobType: Literal['Default', 'Advanced']
    RoleArn: StrictStr
    InputConfig: SageMakerRecommendationJobInputConfig
    JobDescription: StrictStr | None = None
    StoppingConditions: SageMakerRecommendationJobStoppingConditions | None = None
    OutputConfig: SageMakerRecommendationJobOutputConfig | None = None
    Tags: list[SageMakerTagModel] | None = None
