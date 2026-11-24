from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightInvalidTopicReviewedAnswer(BaseModel):
    AnswerId: StrictStr | None = None
    Error: StrictStr | None = None
