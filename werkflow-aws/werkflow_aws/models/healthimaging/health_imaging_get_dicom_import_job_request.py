from __future__ import annotations
from pydantic import BaseModel, StrictStr


class HealthImagingGetDICOMImportJobRequest(BaseModel):
    datastoreId: StrictStr
    jobId: StrictStr
