from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .neptune_filter import NeptuneFilter


class NeptuneDescribeEventCategoriesRequest(BaseModel):
    SourceType: StrictStr | None = None
    Filters: list[NeptuneFilter] | None = None
