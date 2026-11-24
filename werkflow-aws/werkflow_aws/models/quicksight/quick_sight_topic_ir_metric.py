from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_agg_function import QuickSightAggFunction
from .quick_sight_display_format_options import QuickSightDisplayFormatOptions
from .quick_sight_identifier import QuickSightIdentifier
from .quick_sight_named_entity_ref import QuickSightNamedEntityRef
from .quick_sight_topic_ir_comparison_method import QuickSightTopicIRComparisonMethod


class QuickSightTopicIRMetric(BaseModel):
    MetricId: QuickSightIdentifier | None = None
    Function: QuickSightAggFunction | None = None
    Operands: list[QuickSightIdentifier] | None = None
    ComparisonMethod: QuickSightTopicIRComparisonMethod | None = None
    Expression: StrictStr | None = None
    CalculatedFieldReferences: list[QuickSightIdentifier] | None = None
    DisplayFormat: StrictStr | None = None
    DisplayFormatOptions: QuickSightDisplayFormatOptions | None = None
    NamedEntity: QuickSightNamedEntityRef | None = None
