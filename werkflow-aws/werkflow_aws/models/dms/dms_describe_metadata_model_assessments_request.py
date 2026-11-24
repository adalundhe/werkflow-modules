from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .dms_filter import DMSFilter


class DMSDescribeMetadataModelAssessmentsRequest(BaseModel):
    MigrationProjectIdentifier: StrictStr
    Filters: list[DMSFilter] | None = None
    Marker: StrictStr | None = None
    MaxRecords: StrictInt | None = None
