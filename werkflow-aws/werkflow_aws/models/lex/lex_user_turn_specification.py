from __future__ import annotations
from pydantic import BaseModel
from .lex_user_turn_input_specification import LexUserTurnInputSpecification
from .lex_user_turn_output_specification import LexUserTurnOutputSpecification


class LexUserTurnSpecification(BaseModel):
    input: LexUserTurnInputSpecification | None = None
    expected: LexUserTurnOutputSpecification | None = None
