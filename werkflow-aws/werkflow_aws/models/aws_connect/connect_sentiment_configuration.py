from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class ConnectSentimentConfiguration(BaseModel):
    Behavior: Literal['Enable', 'Disable']
