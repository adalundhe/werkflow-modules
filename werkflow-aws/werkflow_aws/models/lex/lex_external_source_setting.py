from __future__ import annotations
from pydantic import BaseModel
from .lex_grammar_slot_type_setting import LexGrammarSlotTypeSetting


class LexExternalSourceSetting(BaseModel):
    grammarSlotTypeSetting: LexGrammarSlotTypeSetting | None = None
