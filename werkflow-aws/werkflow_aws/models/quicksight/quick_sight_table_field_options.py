from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_table_field_option import QuickSightTableFieldOption
from .quick_sight_table_pinned_field_options import QuickSightTablePinnedFieldOptions
from .quick_sight_transposed_table_option import QuickSightTransposedTableOption


class QuickSightTableFieldOptions(BaseModel):
    SelectedFieldOptions: list[QuickSightTableFieldOption] | None = None
    Order: list[StrictStr] | None = None
    PinnedFieldOptions: QuickSightTablePinnedFieldOptions | None = None
    TransposedTableOptions: list[QuickSightTransposedTableOption] | None = None
