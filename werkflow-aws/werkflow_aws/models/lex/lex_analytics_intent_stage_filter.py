from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class LexAnalyticsIntentStageFilter(BaseModel):
    name: Literal['BotAliasId', 'BotVersion', 'LocaleId', 'Modality', 'Channel', 'SessionId', 'OriginatingRequestId', 'IntentName', 'IntentStageName']
    operator: Literal['EQ', 'GT', 'LT']
    values: list[StrictStr]
