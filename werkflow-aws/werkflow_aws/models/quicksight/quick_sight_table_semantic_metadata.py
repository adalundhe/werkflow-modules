from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_shared_column_semantic_metadata import QuickSightSharedColumnSemanticMetadata


class QuickSightTableSemanticMetadata(BaseModel):
    ColumnMetadata: list[QuickSightSharedColumnSemanticMetadata] | None = None
