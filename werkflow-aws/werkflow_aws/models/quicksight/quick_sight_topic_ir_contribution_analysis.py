from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_contribution_analysis_factor import QuickSightContributionAnalysisFactor
from .quick_sight_contribution_analysis_time_ranges import QuickSightContributionAnalysisTimeRanges


class QuickSightTopicIRContributionAnalysis(BaseModel):
    Factors: list[QuickSightContributionAnalysisFactor] | None = None
    TimeRanges: QuickSightContributionAnalysisTimeRanges | None = None
    Direction: StrictStr | None = None
    SortType: StrictStr | None = None
