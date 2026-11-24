from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .personalize_dataset_export_job_output import PersonalizeDatasetExportJobOutput
from .personalize_tag import PersonalizeTag


class PersonalizeCreateDatasetExportJobRequest(BaseModel):
    jobName: StrictStr
    datasetArn: StrictStr
    roleArn: StrictStr
    jobOutput: PersonalizeDatasetExportJobOutput
    ingestionMode: Literal['BULK', 'PUT', 'ALL'] | None = None
    tags: list[PersonalizeTag] | None = None
