from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class LexAnalyticsBinBySpecification(BaseModel):
    name: Literal['ConversationStartTime', 'UtteranceTimestamp']
    interval: Literal['OneHour', 'OneDay']
    order: Literal['Ascending', 'Descending'] | None = None
