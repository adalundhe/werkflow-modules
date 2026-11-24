from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class LexConversationLevelTestResultsFilterBy(BaseModel):
    endToEndResult: Literal['Matched', 'Mismatched', 'ExecutionError'] | None = None
