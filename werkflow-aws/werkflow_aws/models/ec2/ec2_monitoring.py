from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2Monitoring(BaseModel):
    MetricCategoryIds: list[StrictStr] | None = None
    State: StrictStr | None = None
