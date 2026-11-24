from __future__ import annotations
from pydantic import BaseModel
from .lex_intent_statistics import LexIntentStatistics
from .lex_slot_type_statistics import LexSlotTypeStatistics


class LexBotRecommendationResultStatistics(BaseModel):
    intents: LexIntentStatistics | None = None
    slotTypes: LexSlotTypeStatistics | None = None
