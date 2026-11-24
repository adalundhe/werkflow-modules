from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_topic_ir_filter_option import QuickSightTopicIRFilterOption


class QuickSightContributionAnalysisTimeRanges(BaseModel):
    StartRange: QuickSightTopicIRFilterOption | None = None
    EndRange: QuickSightTopicIRFilterOption | None = None
