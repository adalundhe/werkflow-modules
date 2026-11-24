from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class LexBotVersionReplicaSortBy(BaseModel):
    attribute: Literal['BotVersion']
    order: Literal['Ascending', 'Descending']
