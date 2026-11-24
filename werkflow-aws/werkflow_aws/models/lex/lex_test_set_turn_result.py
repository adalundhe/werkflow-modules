from __future__ import annotations
from pydantic import BaseModel
from .lex_agent_turn_result import LexAgentTurnResult
from .lex_user_turn_result import LexUserTurnResult


class LexTestSetTurnResult(BaseModel):
    agent: LexAgentTurnResult | None = None
    user: LexUserTurnResult | None = None
