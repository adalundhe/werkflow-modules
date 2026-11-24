from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .lex_message_group import LexMessageGroup


class LexResponseSpecification(BaseModel):
    messageGroups: list[LexMessageGroup] | None = None
    allowInterrupt: StrictBool | None = None
