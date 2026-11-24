from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class GuardDutyUpdateFindingsFeedbackRequest(BaseModel):
    DetectorId: StrictStr
    FindingIds: list[StrictStr]
    Feedback: Literal['USEFUL', 'NOT_USEFUL']
    Comments: StrictStr | None = None
