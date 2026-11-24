from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .quick_sight_cell_value_synonym import QuickSightCellValueSynonym
from .quick_sight_comparative_order import QuickSightComparativeOrder
from .quick_sight_default_formatting import QuickSightDefaultFormatting
from .quick_sight_semantic_type import QuickSightSemanticType


class QuickSightTopicColumn(BaseModel):
    ColumnName: StrictStr | None = None
    ColumnFriendlyName: StrictStr | None = None
    ColumnDescription: StrictStr | None = None
    ColumnSynonyms: list[StrictStr] | None = None
    ColumnDataRole: StrictStr | None = None
    Aggregation: StrictStr | None = None
    IsIncludedInTopic: StrictBool | None = None
    DisableIndexing: StrictBool | None = None
    ComparativeOrder: QuickSightComparativeOrder | None = None
    SemanticType: QuickSightSemanticType | None = None
    TimeGranularity: StrictStr | None = None
    AllowedAggregations: list[StrictStr] | None = None
    NotAllowedAggregations: list[StrictStr] | None = None
    DefaultFormatting: QuickSightDefaultFormatting | None = None
    NeverAggregateInFilter: StrictBool | None = None
    CellValueSynonyms: list[QuickSightCellValueSynonym] | None = None
    NonAdditive: StrictBool | None = None
