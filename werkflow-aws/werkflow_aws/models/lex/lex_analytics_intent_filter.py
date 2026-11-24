from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class LexAnalyticsIntentFilter(BaseModel):
    name: Literal['BotAliasId', 'BotVersion', 'LocaleId', 'Modality', 'Channel', 'SessionId', 'OriginatingRequestId', 'IntentName', 'IntentEndState']
    operator: Literal['EQ', 'GT', 'LT']
    values: list[StrictStr]
