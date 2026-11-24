from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .quick_sight_cell_value_synonym import QuickSightCellValueSynonym
from .quick_sight_comparative_order import QuickSightComparativeOrder
from .quick_sight_default_formatting import QuickSightDefaultFormatting
from .quick_sight_semantic_type import QuickSightSemanticType


class QuickSightTopicCalculatedField(BaseModel):
    CalculatedFieldName: StrictStr | None = None
    CalculatedFieldDescription: StrictStr | None = None
    Expression: StrictStr | None = None
    CalculatedFieldSynonyms: list[StrictStr] | None = None
    IsIncludedInTopic: StrictBool | None = None
    DisableIndexing: StrictBool | None = None
    ColumnDataRole: StrictStr | None = None
    TimeGranularity: StrictStr | None = None
    DefaultFormatting: QuickSightDefaultFormatting | None = None
    Aggregation: StrictStr | None = None
    ComparativeOrder: QuickSightComparativeOrder | None = None
    SemanticType: QuickSightSemanticType | None = None
    AllowedAggregations: list[StrictStr] | None = None
    NotAllowedAggregations: list[StrictStr] | None = None
    NeverAggregateInFilter: StrictBool | None = None
    CellValueSynonyms: list[QuickSightCellValueSynonym] | None = None
    NonAdditive: StrictBool | None = None
