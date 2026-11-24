from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class LexAnalyticsUtteranceAttribute(BaseModel):
    name: Literal['LastUsedIntent']
