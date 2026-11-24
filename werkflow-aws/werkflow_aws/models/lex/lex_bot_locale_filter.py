from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class LexBotLocaleFilter(BaseModel):
    name: Literal['BotLocaleName']
    values: list[StrictStr]
    operator: Literal['CO', 'EQ']
