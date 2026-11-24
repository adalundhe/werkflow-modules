from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_regional_summary import EC2RegionalSummary


class EC2AttributeSummary(BaseModel):
    AttributeName: StrictStr | None = None
    MostFrequentValue: StrictStr | None = None
    NumberOfMatchedAccounts: StrictInt | None = None
    NumberOfUnmatchedAccounts: StrictInt | None = None
    RegionalSummaries: list[EC2RegionalSummary] | None = None
