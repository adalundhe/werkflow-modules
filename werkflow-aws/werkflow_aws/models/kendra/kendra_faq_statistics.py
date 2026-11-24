from __future__ import annotations
from pydantic import BaseModel, StrictInt


class KendraFaqStatistics(BaseModel):
    IndexedQuestionAnswersCount: StrictInt | None = None
