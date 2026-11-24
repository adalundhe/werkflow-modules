from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConfigServiceDescribeComplianceByConfigRuleRequest(BaseModel):
    ConfigRuleNames: list[StrictStr] | None = None
    ComplianceTypes: list[Literal['COMPLIANT', 'NON_COMPLIANT', 'NOT_APPLICABLE', 'INSUFFICIENT_DATA']] | None = None
    NextToken: StrictStr | None = None
