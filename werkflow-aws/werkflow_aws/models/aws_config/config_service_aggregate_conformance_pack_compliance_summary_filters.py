from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceAggregateConformancePackComplianceSummaryFilters(BaseModel):
    AccountId: StrictStr | None = None
    AwsRegion: StrictStr | None = None
