from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class PersonalizeDatasetImportJobSummary(BaseModel):
    datasetImportJobArn: StrictStr | None = None
    jobName: StrictStr | None = None
    status: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    failureReason: StrictStr | None = None
    importMode: StrictStr | None = None
