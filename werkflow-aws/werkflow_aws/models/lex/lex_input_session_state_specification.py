from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_active_context import LexActiveContext
from .lex_runtime_hints import LexRuntimeHints


class LexInputSessionStateSpecification(BaseModel):
    sessionAttributes: dict[StrictStr, StrictStr] | None = None
    activeContexts: list[LexActiveContext] | None = None
    runtimeHints: LexRuntimeHints | None = None
