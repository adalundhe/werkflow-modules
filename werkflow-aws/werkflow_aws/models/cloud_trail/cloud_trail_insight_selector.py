from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailInsightSelector(BaseModel):
    InsightType: StrictStr | None = None
    EventCategories: list[StrictStr] | None = None
