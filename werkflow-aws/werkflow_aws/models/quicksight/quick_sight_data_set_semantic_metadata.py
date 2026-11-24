from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_custom_instruction import QuickSightCustomInstruction
from .quick_sight_data_set_semantic_description import QuickSightDataSetSemanticDescription


class QuickSightDataSetSemanticMetadata(BaseModel):
    Description: QuickSightDataSetSemanticDescription | None = None
    CustomInstructions: list[QuickSightCustomInstruction] | None = None
