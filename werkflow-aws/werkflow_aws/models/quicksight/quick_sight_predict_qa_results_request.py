from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightPredictQAResultsRequest(BaseModel):
    AwsAccountId: StrictStr
    QueryText: StrictStr
    IncludeQuickSightQIndex: Literal['INCLUDE', 'EXCLUDE'] | None = None
    IncludeGeneratedAnswer: Literal['INCLUDE', 'EXCLUDE'] | None = None
    MaxTopicsToConsider: StrictInt | None = None
