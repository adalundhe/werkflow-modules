from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class QuickSightAnalysisSearchFilter(BaseModel):
    Operator: Literal['StringEquals', 'StringLike'] | None = None
    Name: Literal['QUICKSIGHT_USER', 'QUICKSIGHT_VIEWER_OR_OWNER', 'DIRECT_QUICKSIGHT_VIEWER_OR_OWNER', 'QUICKSIGHT_OWNER', 'DIRECT_QUICKSIGHT_OWNER', 'DIRECT_QUICKSIGHT_SOLE_OWNER', 'ANALYSIS_NAME'] | None = None
    Value: StrictStr | None = None
