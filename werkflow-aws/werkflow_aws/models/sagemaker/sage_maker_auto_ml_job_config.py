from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_auto_ml_candidate_generation_config import SageMakerAutoMLCandidateGenerationConfig
from .sage_maker_auto_ml_data_split_config import SageMakerAutoMLDataSplitConfig
from .sage_maker_auto_ml_job_completion_criteria import SageMakerAutoMLJobCompletionCriteria
from .sage_maker_auto_ml_security_config import SageMakerAutoMLSecurityConfig


class SageMakerAutoMLJobConfig(BaseModel):
    CompletionCriteria: SageMakerAutoMLJobCompletionCriteria | None = None
    SecurityConfig: SageMakerAutoMLSecurityConfig | None = None
    CandidateGenerationConfig: SageMakerAutoMLCandidateGenerationConfig | None = None
    DataSplitConfig: SageMakerAutoMLDataSplitConfig | None = None
    Mode: StrictStr | None = None
