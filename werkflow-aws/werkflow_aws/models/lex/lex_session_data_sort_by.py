from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class LexSessionDataSortBy(BaseModel):
    name: Literal['ConversationStartTime', 'NumberOfTurns', 'Duration']
    order: Literal['Ascending', 'Descending']
