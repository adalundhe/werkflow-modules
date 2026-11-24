from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_data_qn_a_configurations import QuickSightDataQnAConfigurations
from .quick_sight_data_stories_configurations import QuickSightDataStoriesConfigurations
from .quick_sight_executive_summary_configurations import QuickSightExecutiveSummaryConfigurations
from .quick_sight_generative_authoring_configurations import QuickSightGenerativeAuthoringConfigurations


class QuickSightAmazonQInQuickSightConsoleConfigurations(BaseModel):
    DataQnA: QuickSightDataQnAConfigurations | None = None
    GenerativeAuthoring: QuickSightGenerativeAuthoringConfigurations | None = None
    ExecutiveSummary: QuickSightExecutiveSummaryConfigurations | None = None
    DataStories: QuickSightDataStoriesConfigurations | None = None
