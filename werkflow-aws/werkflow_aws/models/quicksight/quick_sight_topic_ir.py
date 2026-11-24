from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_topic_ir_contribution_analysis import QuickSightTopicIRContributionAnalysis
from .quick_sight_topic_ir_filter_option import QuickSightTopicIRFilterOption
from .quick_sight_topic_ir_group_by import QuickSightTopicIRGroupBy
from .quick_sight_topic_ir_metric import QuickSightTopicIRMetric
from .quick_sight_topic_sort_clause import QuickSightTopicSortClause
from .quick_sight_visual_options import QuickSightVisualOptions


class QuickSightTopicIR(BaseModel):
    Metrics: list[QuickSightTopicIRMetric] | None = None
    GroupByList: list[QuickSightTopicIRGroupBy] | None = None
    Filters: list[list[QuickSightTopicIRFilterOption]] | None = None
    Sort: QuickSightTopicSortClause | None = None
    ContributionAnalysis: QuickSightTopicIRContributionAnalysis | None = None
    Visual: QuickSightVisualOptions | None = None
