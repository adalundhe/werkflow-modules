from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .personalize_data_source import PersonalizeDataSource


class PersonalizeDatasetImportJob(BaseModel):
    jobName: StrictStr | None = None
    datasetImportJobArn: StrictStr | None = None
    datasetArn: StrictStr | None = None
    dataSource: PersonalizeDataSource | None = None
    roleArn: StrictStr | None = None
    status: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    failureReason: StrictStr | None = None
    importMode: StrictStr | None = None
    publishAttributionMetricsToS3: StrictBool | None = None
