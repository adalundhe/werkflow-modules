from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class DevOpsGuruListInsightsOngoingStatusFilter(BaseModel):
    Type: Literal['REACTIVE', 'PROACTIVE']
