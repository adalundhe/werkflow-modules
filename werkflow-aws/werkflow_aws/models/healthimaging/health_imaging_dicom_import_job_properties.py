from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .health_imaging_import_configuration import HealthImagingImportConfiguration


class HealthImagingDICOMImportJobProperties(BaseModel):
    jobId: StrictStr | None = None
    jobName: StrictStr | None = None
    jobStatus: StrictStr | None = None
    datastoreId: StrictStr | None = None
    dataAccessRoleArn: StrictStr | None = None
    endedAt: datetime.datetime | StrictStr | None = None
    submittedAt: datetime.datetime | StrictStr | None = None
    inputS3Uri: StrictStr | None = None
    outputS3Uri: StrictStr | None = None
    message: StrictStr | None = None
    importConfiguration: HealthImagingImportConfiguration | None = None
