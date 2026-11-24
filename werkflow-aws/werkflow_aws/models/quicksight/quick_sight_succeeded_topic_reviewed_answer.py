from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightSucceededTopicReviewedAnswer(BaseModel):
    AnswerId: StrictStr | None = None
