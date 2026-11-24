from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_pivot_table_conditional_formatting_scope import QuickSightPivotTableConditionalFormattingScope
from .quick_sight_text_conditional_format import QuickSightTextConditionalFormat


class QuickSightPivotTableCellConditionalFormatting(BaseModel):
    FieldId: StrictStr | None = None
    TextFormat: QuickSightTextConditionalFormat | None = None
    Scope: QuickSightPivotTableConditionalFormattingScope | None = None
    Scopes: list[QuickSightPivotTableConditionalFormattingScope] | None = None
