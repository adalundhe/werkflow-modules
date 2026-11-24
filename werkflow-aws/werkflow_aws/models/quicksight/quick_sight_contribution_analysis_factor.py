from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightContributionAnalysisFactor(BaseModel):
    FieldName: StrictStr | None = None
