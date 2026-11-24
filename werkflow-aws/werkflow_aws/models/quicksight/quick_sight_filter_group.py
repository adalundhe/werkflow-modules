from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_filter import QuickSightFilter
from .quick_sight_filter_scope_configuration import QuickSightFilterScopeConfiguration


class QuickSightFilterGroup(BaseModel):
    FilterGroupId: StrictStr | None = None
    Filters: list[QuickSightFilter] | None = None
    ScopeConfiguration: QuickSightFilterScopeConfiguration | None = None
    Status: StrictStr | None = None
    CrossDataset: StrictStr | None = None
