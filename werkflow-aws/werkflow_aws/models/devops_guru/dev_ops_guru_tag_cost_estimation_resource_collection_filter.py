from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DevOpsGuruTagCostEstimationResourceCollectionFilter(BaseModel):
    AppBoundaryKey: StrictStr | None = None
    TagValues: list[StrictStr] | None = None
