from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class LexBotLocaleSortBy(BaseModel):
    attribute: Literal['BotLocaleName']
    order: Literal['Ascending', 'Descending']
