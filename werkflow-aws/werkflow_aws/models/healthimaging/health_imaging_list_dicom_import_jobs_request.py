from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class HealthImagingListDICOMImportJobsRequest(BaseModel):
    datastoreId: StrictStr
    jobStatus: Literal['SUBMITTED', 'IN_PROGRESS', 'COMPLETED', 'FAILED'] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
