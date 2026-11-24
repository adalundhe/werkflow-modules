from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .personalize_data_source import PersonalizeDataSource
from .personalize_tag import PersonalizeTag


class PersonalizeCreateDataDeletionJobRequest(BaseModel):
    jobName: StrictStr
    datasetGroupArn: StrictStr
    dataSource: PersonalizeDataSource
    roleArn: StrictStr
    tags: list[PersonalizeTag] | None = None
