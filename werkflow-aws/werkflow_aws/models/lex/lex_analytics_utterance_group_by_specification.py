from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class LexAnalyticsUtteranceGroupBySpecification(BaseModel):
    name: Literal['UtteranceText', 'UtteranceState']
