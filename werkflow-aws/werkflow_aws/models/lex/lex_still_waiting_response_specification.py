from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt
from .lex_message_group import LexMessageGroup


class LexStillWaitingResponseSpecification(BaseModel):
    messageGroups: list[LexMessageGroup] | None = None
    frequencyInSeconds: StrictInt | None = None
    timeoutInSeconds: StrictInt | None = None
    allowInterrupt: StrictBool | None = None
