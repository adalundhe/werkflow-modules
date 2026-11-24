from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_recommendation_job_compiled_output_config import SageMakerRecommendationJobCompiledOutputConfig


class SageMakerRecommendationJobOutputConfig(BaseModel):
    KmsKeyId: StrictStr | None = None
    CompiledOutputConfig: SageMakerRecommendationJobCompiledOutputConfig | None = None
