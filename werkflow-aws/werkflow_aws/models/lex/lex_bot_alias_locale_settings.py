from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .lex_code_hook_specification import LexCodeHookSpecification


class LexBotAliasLocaleSettings(BaseModel):
    enabled: StrictBool | None = None
    codeHookSpecification: LexCodeHookSpecification | None = None
