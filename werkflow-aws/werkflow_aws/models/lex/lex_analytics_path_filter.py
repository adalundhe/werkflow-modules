from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class LexAnalyticsPathFilter(BaseModel):
    name: Literal['BotAliasId', 'BotVersion', 'LocaleId', 'Modality', 'Channel']
    operator: Literal['EQ', 'GT', 'LT']
    values: list[StrictStr]
