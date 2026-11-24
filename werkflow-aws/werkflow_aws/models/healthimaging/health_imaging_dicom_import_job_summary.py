from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class HealthImagingDICOMImportJobSummary(BaseModel):
    jobId: StrictStr | None = None
    jobName: StrictStr | None = None
    jobStatus: StrictStr | None = None
    datastoreId: StrictStr | None = None
    dataAccessRoleArn: StrictStr | None = None
    endedAt: datetime.datetime | StrictStr | None = None
    submittedAt: datetime.datetime | StrictStr | None = None
    message: StrictStr | None = None
