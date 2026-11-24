from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .lex_intent_disambiguation_settings import LexIntentDisambiguationSettings


class LexNluImprovementSpecification(BaseModel):
    enabled: StrictBool | None = None
    assistedNluMode: StrictStr | None = None
    intentDisambiguationSettings: LexIntentDisambiguationSettings | None = None
