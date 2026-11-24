from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class LexAnalyticsUtteranceFilter(BaseModel):
    name: Literal['BotAliasId', 'BotVersion', 'LocaleId', 'Modality', 'Channel', 'SessionId', 'OriginatingRequestId', 'UtteranceState', 'UtteranceText']
    operator: Literal['EQ', 'GT', 'LT']
    values: list[StrictStr]
