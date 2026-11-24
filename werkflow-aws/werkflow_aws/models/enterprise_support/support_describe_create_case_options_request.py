from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SupportDescribeCreateCaseOptionsRequest(BaseModel):
    issueType: StrictStr
    serviceCode: StrictStr
    language: StrictStr
    categoryCode: StrictStr
    dryRun: StrictBool | None = None
