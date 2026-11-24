from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_column_identifier import QuickSightColumnIdentifier


class QuickSightContributionAnalysisDefault(BaseModel):
    MeasureFieldId: StrictStr | None = None
    ContributorDimensions: list[QuickSightColumnIdentifier] | None = None
