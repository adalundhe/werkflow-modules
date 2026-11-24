from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubInsightResultValue(BaseModel):
    GroupByAttributeValue: StrictStr | None = None
    Count: StrictInt | None = None
