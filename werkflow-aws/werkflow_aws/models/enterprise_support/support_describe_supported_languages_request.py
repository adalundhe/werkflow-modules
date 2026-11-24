from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SupportDescribeSupportedLanguagesRequest(BaseModel):
    issueType: StrictStr
    serviceCode: StrictStr
    categoryCode: StrictStr
    dryRun: StrictBool | None = None
