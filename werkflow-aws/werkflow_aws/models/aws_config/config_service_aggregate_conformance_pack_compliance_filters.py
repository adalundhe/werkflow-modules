from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConfigServiceAggregateConformancePackComplianceFilters(BaseModel):
    ConformancePackName: StrictStr | None = None
    ComplianceType: Literal['COMPLIANT', 'NON_COMPLIANT', 'INSUFFICIENT_DATA'] | None = None
    AccountId: StrictStr | None = None
    AwsRegion: StrictStr | None = None
