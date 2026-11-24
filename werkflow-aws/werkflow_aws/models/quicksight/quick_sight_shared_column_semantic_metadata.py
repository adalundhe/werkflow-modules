from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_column_semantic_property import QuickSightColumnSemanticProperty


class QuickSightSharedColumnSemanticMetadata(BaseModel):
    ColumnNames: list[StrictStr] | None = None
    ColumnProperties: list[QuickSightColumnSemanticProperty] | None = None
