from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .iam_access_detail import IAMAccessDetail
from .iam_error_details import IAMErrorDetails


class IAMGetOrganizationsAccessReportResponse(BaseModel):
    JobStatus: StrictStr | None = None
    JobCreationDate: datetime.datetime | StrictStr | None = None
    JobCompletionDate: datetime.datetime | StrictStr | None = None
    NumberOfServicesAccessible: StrictInt | None = None
    NumberOfServicesNotAccessed: StrictInt | None = None
    AccessDetails: list[IAMAccessDetail] | None = None
    IsTruncated: StrictBool | None = None
    Marker: StrictStr | None = None
    ErrorDetails: IAMErrorDetails | None = None
    ResponseMetadata: dict[str, Any] | None = None
