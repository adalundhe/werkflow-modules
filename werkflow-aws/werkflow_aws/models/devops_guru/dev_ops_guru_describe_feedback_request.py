from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DevOpsGuruDescribeFeedbackRequest(BaseModel):
    InsightId: StrictStr | None = None
