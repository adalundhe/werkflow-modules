from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexAnalyticsIntentStageGroupByKey(BaseModel):
    name: StrictStr | None = None
    value: StrictStr | None = None
