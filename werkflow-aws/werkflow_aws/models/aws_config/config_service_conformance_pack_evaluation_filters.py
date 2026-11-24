from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConfigServiceConformancePackEvaluationFilters(BaseModel):
    ConfigRuleNames: list[StrictStr] | None = None
    ComplianceType: Literal['COMPLIANT', 'NON_COMPLIANT', 'INSUFFICIENT_DATA'] | None = None
    ResourceType: StrictStr | None = None
    ResourceIds: list[StrictStr] | None = None
