from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESReviewDetails(BaseModel):
    Status: StrictStr | None = None
    CaseId: StrictStr | None = None
