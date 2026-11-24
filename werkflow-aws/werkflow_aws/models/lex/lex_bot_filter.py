from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class LexBotFilter(BaseModel):
    name: Literal['BotName', 'BotType']
    values: list[StrictStr]
    operator: Literal['CO', 'EQ', 'NE']
