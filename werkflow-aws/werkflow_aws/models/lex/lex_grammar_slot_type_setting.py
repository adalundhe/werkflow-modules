from __future__ import annotations
from pydantic import BaseModel
from .lex_grammar_slot_type_source import LexGrammarSlotTypeSource


class LexGrammarSlotTypeSetting(BaseModel):
    source: LexGrammarSlotTypeSource | None = None
