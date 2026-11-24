from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr


class QBusinessMessageUsefulnessFeedback(BaseModel):
    usefulness: Literal['USEFUL', 'NOT_USEFUL']
    submittedAt: datetime.datetime | StrictStr
    reason: Literal['NOT_FACTUALLY_CORRECT', 'HARMFUL_OR_UNSAFE', 'INCORRECT_OR_MISSING_SOURCES', 'NOT_HELPFUL', 'FACTUALLY_CORRECT', 'COMPLETE', 'RELEVANT_SOURCES', 'HELPFUL', 'NOT_BASED_ON_DOCUMENTS', 'NOT_COMPLETE', 'NOT_CONCISE', 'OTHER'] | None = None
    comment: StrictStr | None = None
