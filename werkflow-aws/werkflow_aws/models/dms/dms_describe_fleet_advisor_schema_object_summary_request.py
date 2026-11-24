from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .dms_filter import DMSFilter


class DMSDescribeFleetAdvisorSchemaObjectSummaryRequest(BaseModel):
    Filters: list[DMSFilter] | None = None
    MaxRecords: StrictInt | None = None
    NextToken: StrictStr | None = None
