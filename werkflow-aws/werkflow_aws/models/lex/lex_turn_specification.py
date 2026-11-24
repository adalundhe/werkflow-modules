from __future__ import annotations
from pydantic import BaseModel
from .lex_agent_turn_specification import LexAgentTurnSpecification
from .lex_user_turn_specification import LexUserTurnSpecification


class LexTurnSpecification(BaseModel):
    agentTurn: LexAgentTurnSpecification | None = None
    userTurn: LexUserTurnSpecification | None = None
