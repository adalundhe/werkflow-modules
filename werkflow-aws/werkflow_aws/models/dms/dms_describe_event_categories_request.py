from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dms_filter import DMSFilter


class DMSDescribeEventCategoriesRequest(BaseModel):
    SourceType: StrictStr | None = None
    Filters: list[DMSFilter] | None = None
