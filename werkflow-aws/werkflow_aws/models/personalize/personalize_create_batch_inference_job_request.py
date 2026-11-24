from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .personalize_batch_inference_job_config import PersonalizeBatchInferenceJobConfig
from .personalize_batch_inference_job_input import PersonalizeBatchInferenceJobInput
from .personalize_batch_inference_job_output import PersonalizeBatchInferenceJobOutput
from .personalize_tag import PersonalizeTag
from .personalize_theme_generation_config import PersonalizeThemeGenerationConfig


class PersonalizeCreateBatchInferenceJobRequest(BaseModel):
    jobName: StrictStr
    solutionVersionArn: StrictStr
    jobInput: PersonalizeBatchInferenceJobInput
    jobOutput: PersonalizeBatchInferenceJobOutput
    roleArn: StrictStr
    filterArn: StrictStr | None = None
    numResults: StrictInt | None = None
    batchInferenceJobConfig: PersonalizeBatchInferenceJobConfig | None = None
    tags: list[PersonalizeTag] | None = None
    batchInferenceJobMode: Literal['BATCH_INFERENCE', 'THEME_GENERATION'] | None = None
    themeGenerationConfig: PersonalizeThemeGenerationConfig | None = None
