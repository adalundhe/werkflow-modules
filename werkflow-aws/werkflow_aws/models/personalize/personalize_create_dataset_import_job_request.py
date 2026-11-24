from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .personalize_data_source import PersonalizeDataSource
from .personalize_tag import PersonalizeTag


class PersonalizeCreateDatasetImportJobRequest(BaseModel):
    jobName: StrictStr
    datasetArn: StrictStr
    dataSource: PersonalizeDataSource
    roleArn: StrictStr | None = None
    tags: list[PersonalizeTag] | None = None
    importMode: Literal['FULL', 'INCREMENTAL'] | None = None
    publishAttributionMetricsToS3: StrictBool | None = None
