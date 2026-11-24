from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .health_imaging_import_configuration import HealthImagingImportConfiguration


class HealthImagingStartDICOMImportJobRequest(BaseModel):
    dataAccessRoleArn: StrictStr
    clientToken: StrictStr
    datastoreId: StrictStr
    inputS3Uri: StrictStr
    outputS3Uri: StrictStr
    jobName: StrictStr | None = None
    inputOwnerAccountId: StrictStr | None = None
    importConfiguration: HealthImagingImportConfiguration | None = None
