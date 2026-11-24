from __future__ import annotations
from pydantic import BaseModel
from .lex_bot_alias_test_execution_target import LexBotAliasTestExecutionTarget


class LexTestExecutionTarget(BaseModel):
    botAliasTarget: LexBotAliasTestExecutionTarget | None = None
