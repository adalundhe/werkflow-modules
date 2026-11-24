from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class KendraRelevanceFeedback(BaseModel):
    ResultId: StrictStr
    RelevanceValue: Literal['RELEVANT', 'NOT_RELEVANT']
