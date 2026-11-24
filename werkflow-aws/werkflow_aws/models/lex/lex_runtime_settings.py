from __future__ import annotations
from pydantic import BaseModel
from .lex_nlu_improvement_specification import LexNluImprovementSpecification
from .lex_slot_resolution_improvement_specification import LexSlotResolutionImprovementSpecification


class LexRuntimeSettings(BaseModel):
    slotResolutionImprovement: LexSlotResolutionImprovementSpecification | None = None
    nluImprovement: LexNluImprovementSpecification | None = None
