from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_data_set_semantic_metadata import QuickSightDataSetSemanticMetadata
from .quick_sight_semantic_table import QuickSightSemanticTable


class QuickSightSemanticModelConfiguration(BaseModel):
    TableMap: dict[StrictStr, QuickSightSemanticTable] | None = None
    SemanticMetadata: list[QuickSightDataSetSemanticMetadata] | None = None
