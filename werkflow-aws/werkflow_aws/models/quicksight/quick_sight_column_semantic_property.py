from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_additional_notes import QuickSightAdditionalNotes
from .quick_sight_column_description import QuickSightColumnDescription
from .quick_sight_column_semantic_type import QuickSightColumnSemanticType


class QuickSightColumnSemanticProperty(BaseModel):
    Description: QuickSightColumnDescription | None = None
    AdditionalNotes: QuickSightAdditionalNotes | None = None
    SemanticType: QuickSightColumnSemanticType | None = None
