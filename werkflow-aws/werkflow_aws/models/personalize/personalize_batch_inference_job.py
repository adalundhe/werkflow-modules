from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .personalize_batch_inference_job_config import PersonalizeBatchInferenceJobConfig
from .personalize_batch_inference_job_input import PersonalizeBatchInferenceJobInput
from .personalize_batch_inference_job_output import PersonalizeBatchInferenceJobOutput
from .personalize_theme_generation_config import PersonalizeThemeGenerationConfig


class PersonalizeBatchInferenceJob(BaseModel):
    jobName: StrictStr | None = None
    batchInferenceJobArn: StrictStr | None = None
    filterArn: StrictStr | None = None
    failureReason: StrictStr | None = None
    solutionVersionArn: StrictStr | None = None
    numResults: StrictInt | None = None
    jobInput: PersonalizeBatchInferenceJobInput | None = None
    jobOutput: PersonalizeBatchInferenceJobOutput | None = None
    batchInferenceJobConfig: PersonalizeBatchInferenceJobConfig | None = None
    roleArn: StrictStr | None = None
    batchInferenceJobMode: StrictStr | None = None
    themeGenerationConfig: PersonalizeThemeGenerationConfig | None = None
    status: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
