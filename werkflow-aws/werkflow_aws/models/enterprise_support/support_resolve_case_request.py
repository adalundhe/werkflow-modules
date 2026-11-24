from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SupportResolveCaseRequest(BaseModel):
    caseId: StrictStr | None = None
    dryRun: StrictBool | None = None
