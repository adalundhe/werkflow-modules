from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class LexBotSortBy(BaseModel):
    attribute: Literal['BotName']
    order: Literal['Ascending', 'Descending']
