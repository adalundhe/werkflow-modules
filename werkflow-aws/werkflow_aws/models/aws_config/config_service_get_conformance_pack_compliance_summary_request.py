from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConfigServiceGetConformancePackComplianceSummaryRequest(BaseModel):
    ConformancePackNames: list[StrictStr]
    Limit: StrictInt | None = None
    NextToken: StrictStr | None = None
