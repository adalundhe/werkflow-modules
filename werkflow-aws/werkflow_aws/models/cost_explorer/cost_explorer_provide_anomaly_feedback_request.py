from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CostExplorerProvideAnomalyFeedbackRequest(BaseModel):
    AnomalyId: StrictStr
    Feedback: Literal['YES', 'NO', 'PLANNED_ACTIVITY']
