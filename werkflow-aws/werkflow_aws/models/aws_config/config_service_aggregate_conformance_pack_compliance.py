from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConfigServiceAggregateConformancePackCompliance(BaseModel):
    ComplianceType: StrictStr | None = None
    CompliantRuleCount: StrictInt | None = None
    NonCompliantRuleCount: StrictInt | None = None
    TotalRuleCount: StrictInt | None = None
