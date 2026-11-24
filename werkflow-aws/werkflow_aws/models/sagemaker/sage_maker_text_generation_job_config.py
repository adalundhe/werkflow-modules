from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_auto_ml_job_completion_criteria import SageMakerAutoMLJobCompletionCriteria
from .sage_maker_model_access_config_model import SageMakerModelAccessConfigModel


class SageMakerTextGenerationJobConfig(BaseModel):
    CompletionCriteria: SageMakerAutoMLJobCompletionCriteria | None = None
    BaseModelName: StrictStr | None = None
    TextGenerationHyperParameters: dict[StrictStr, StrictStr] | None = None
    ModelAccessConfig: SageMakerModelAccessConfigModel | None = None
