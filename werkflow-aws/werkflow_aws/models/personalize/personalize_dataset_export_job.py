from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .personalize_dataset_export_job_output import PersonalizeDatasetExportJobOutput


class PersonalizeDatasetExportJob(BaseModel):
    jobName: StrictStr | None = None
    datasetExportJobArn: StrictStr | None = None
    datasetArn: StrictStr | None = None
    ingestionMode: StrictStr | None = None
    roleArn: StrictStr | None = None
    status: StrictStr | None = None
    jobOutput: PersonalizeDatasetExportJobOutput | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    failureReason: StrictStr | None = None
