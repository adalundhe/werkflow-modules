from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudWatchInsightRule(BaseModel):
    Name: StrictStr | None = None
    State: StrictStr | None = None
    Schema: StrictStr | None = None
    Definition: StrictStr | None = None
    ManagedRule: StrictBool | None = None
    ApplyOnTransformedLogs: StrictBool | None = None
