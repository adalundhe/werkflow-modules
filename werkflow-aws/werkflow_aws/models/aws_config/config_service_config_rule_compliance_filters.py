from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConfigServiceConfigRuleComplianceFilters(BaseModel):
    ConfigRuleName: StrictStr | None = None
    ComplianceType: Literal['COMPLIANT', 'NON_COMPLIANT', 'NOT_APPLICABLE', 'INSUFFICIENT_DATA'] | None = None
    AccountId: StrictStr | None = None
    AwsRegion: StrictStr | None = None
