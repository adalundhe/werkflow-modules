from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .iam_entity_details import IAMEntityDetails
from .iam_error_details import IAMErrorDetails


class IAMGetServiceLastAccessedDetailsWithEntitiesResponse(BaseModel):
    JobStatus: StrictStr | None = None
    JobCreationDate: datetime.datetime | StrictStr | None = None
    JobCompletionDate: datetime.datetime | StrictStr | None = None
    EntityDetailsList: list[IAMEntityDetails] | None = None
    IsTruncated: StrictBool | None = None
    Marker: StrictStr | None = None
    Error: IAMErrorDetails | None = None
    ResponseMetadata: dict[str, Any] | None = None
