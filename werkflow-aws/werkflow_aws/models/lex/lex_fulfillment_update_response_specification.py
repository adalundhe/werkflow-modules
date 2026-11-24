from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt
from .lex_message_group import LexMessageGroup


class LexFulfillmentUpdateResponseSpecification(BaseModel):
    frequencyInSeconds: StrictInt | None = None
    messageGroups: list[LexMessageGroup] | None = None
    allowInterrupt: StrictBool | None = None
