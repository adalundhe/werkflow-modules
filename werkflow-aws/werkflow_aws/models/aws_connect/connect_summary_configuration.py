from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class ConnectSummaryConfiguration(BaseModel):
    SummaryModes: list[Literal['PostContact', 'AutomatedInteraction', 'ContactChain']]
