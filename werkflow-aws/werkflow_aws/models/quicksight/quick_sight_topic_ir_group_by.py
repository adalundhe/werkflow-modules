from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_display_format_options import QuickSightDisplayFormatOptions
from .quick_sight_identifier import QuickSightIdentifier
from .quick_sight_named_entity_ref import QuickSightNamedEntityRef
from .quick_sight_topic_sort_clause import QuickSightTopicSortClause


class QuickSightTopicIRGroupBy(BaseModel):
    FieldName: QuickSightIdentifier | None = None
    TimeGranularity: StrictStr | None = None
    Sort: QuickSightTopicSortClause | None = None
    DisplayFormat: StrictStr | None = None
    DisplayFormatOptions: QuickSightDisplayFormatOptions | None = None
    NamedEntity: QuickSightNamedEntityRef | None = None
