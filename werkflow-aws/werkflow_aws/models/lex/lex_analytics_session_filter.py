from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class LexAnalyticsSessionFilter(BaseModel):
    name: Literal['BotAliasId', 'BotVersion', 'LocaleId', 'Modality', 'Channel', 'Duration', 'ConversationEndState', 'SessionId', 'OriginatingRequestId', 'IntentPath']
    operator: Literal['EQ', 'GT', 'LT']
    values: list[StrictStr]
