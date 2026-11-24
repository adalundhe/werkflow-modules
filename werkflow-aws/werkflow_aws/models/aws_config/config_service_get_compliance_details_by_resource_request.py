from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConfigServiceGetComplianceDetailsByResourceRequest(BaseModel):
    ResourceType: StrictStr | None = None
    ResourceId: StrictStr | None = None
    ComplianceTypes: list[Literal['COMPLIANT', 'NON_COMPLIANT', 'NOT_APPLICABLE', 'INSUFFICIENT_DATA']] | None = None
    NextToken: StrictStr | None = None
    ResourceEvaluationId: StrictStr | None = None
