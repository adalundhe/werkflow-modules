from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class HealthImagingStartDICOMImportJobResponse(BaseModel):
    datastoreId: StrictStr | None = None
    jobId: StrictStr | None = None
    jobStatus: StrictStr | None = None
    submittedAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
