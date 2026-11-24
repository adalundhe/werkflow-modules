from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_input_session_state_specification import LexInputSessionStateSpecification
from .lex_utterance_input_specification import LexUtteranceInputSpecification


class LexUserTurnInputSpecification(BaseModel):
    utteranceInput: LexUtteranceInputSpecification | None = None
    requestAttributes: dict[StrictStr, StrictStr] | None = None
    sessionState: LexInputSessionStateSpecification | None = None
