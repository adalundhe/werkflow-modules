from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_auto_ml_job_completion_criteria import SageMakerAutoMLJobCompletionCriteria
from .sage_maker_candidate_generation_config import SageMakerCandidateGenerationConfig


class SageMakerTabularJobConfig(BaseModel):
    CandidateGenerationConfig: SageMakerCandidateGenerationConfig | None = None
    CompletionCriteria: SageMakerAutoMLJobCompletionCriteria | None = None
    FeatureSpecificationS3Uri: StrictStr | None = None
    Mode: StrictStr | None = None
    GenerateCandidateDefinitionsOnly: StrictBool | None = None
    ProblemType: StrictStr | None = None
    TargetAttributeName: StrictStr | None = None
    SampleWeightAttributeName: StrictStr | None = None
