from __future__ import annotations
from pydantic import BaseModel
from .lex_message import LexMessage


class LexMessageGroup(BaseModel):
    message: LexMessage | None = None
    variations: list[LexMessage] | None = None
