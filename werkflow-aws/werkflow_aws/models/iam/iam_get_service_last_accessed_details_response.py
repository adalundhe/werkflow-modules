from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .iam_error_details import IAMErrorDetails
from .iam_service_last_accessed import IAMServiceLastAccessed


class IAMGetServiceLastAccessedDetailsResponse(BaseModel):
    JobStatus: StrictStr | None = None
    JobType: StrictStr | None = None
    JobCreationDate: datetime.datetime | StrictStr | None = None
    ServicesLastAccessed: list[IAMServiceLastAccessed] | None = None
    JobCompletionDate: datetime.datetime | StrictStr | None = None
    IsTruncated: StrictBool | None = None
    Marker: StrictStr | None = None
    Error: IAMErrorDetails | None = None
    ResponseMetadata: dict[str, Any] | None = None
