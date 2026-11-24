from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceConformancePackRuleCompliance(BaseModel):
    ConfigRuleName: StrictStr | None = None
    ComplianceType: StrictStr | None = None
    Controls: list[StrictStr] | None = None
