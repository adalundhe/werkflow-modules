from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ConfigServiceGetAggregateComplianceDetailsByConfigRuleRequest(BaseModel):
    ConfigurationAggregatorName: StrictStr
    ConfigRuleName: StrictStr
    AccountId: StrictStr
    AwsRegion: StrictStr
    ComplianceType: Literal['COMPLIANT', 'NON_COMPLIANT', 'NOT_APPLICABLE', 'INSUFFICIENT_DATA'] | None = None
    Limit: StrictInt | None = None
    NextToken: StrictStr | None = None
