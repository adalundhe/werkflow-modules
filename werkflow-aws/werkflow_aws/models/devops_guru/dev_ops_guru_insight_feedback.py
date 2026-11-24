from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DevOpsGuruInsightFeedback(BaseModel):
    Id: StrictStr | None = None
    Feedback: StrictStr | None = None
