from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class LexAnalyticsSessionGroupBySpecification(BaseModel):
    name: Literal['ConversationEndState', 'LocaleId']
