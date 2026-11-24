from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .personalize_data_source import PersonalizeDataSource


class PersonalizeDataDeletionJob(BaseModel):
    jobName: StrictStr | None = None
    dataDeletionJobArn: StrictStr | None = None
    datasetGroupArn: StrictStr | None = None
    dataSource: PersonalizeDataSource | None = None
    roleArn: StrictStr | None = None
    status: StrictStr | None = None
    numDeleted: StrictInt | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    failureReason: StrictStr | None = None
