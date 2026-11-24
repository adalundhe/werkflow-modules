from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SupportDescribeSeverityLevelsRequest(BaseModel):
    language: StrictStr | None = None
    dryRun: StrictBool | None = None
