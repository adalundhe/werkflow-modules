from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .quick_sight_aggregation_partition_by import QuickSightAggregationPartitionBy
from .quick_sight_anchor import QuickSightAnchor
from .quick_sight_filter_agg_metrics import QuickSightFilterAggMetrics
from .quick_sight_identifier import QuickSightIdentifier
from .quick_sight_topic_constant_value import QuickSightTopicConstantValue


class QuickSightTopicIRFilterOption(BaseModel):
    FilterType: StrictStr | None = None
    FilterClass: StrictStr | None = None
    OperandField: QuickSightIdentifier | None = None
    Function: StrictStr | None = None
    Constant: QuickSightTopicConstantValue | None = None
    Inverse: StrictBool | None = None
    NullFilter: StrictStr | None = None
    Aggregation: StrictStr | None = None
    AggregationFunctionParameters: dict[StrictStr, StrictStr] | None = None
    AggregationPartitionBy: list[QuickSightAggregationPartitionBy] | None = None
    Range: QuickSightTopicConstantValue | None = None
    Inclusive: StrictBool | None = None
    TimeGranularity: StrictStr | None = None
    LastNextOffset: QuickSightTopicConstantValue | None = None
    AggMetrics: list[QuickSightFilterAggMetrics] | None = None
    TopBottomLimit: QuickSightTopicConstantValue | None = None
    SortDirection: StrictStr | None = None
    Anchor: QuickSightAnchor | None = None
