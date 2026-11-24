from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class ConnectContactMetricInfo(BaseModel):
    Name: Literal['ESTIMATED_WAIT_TIME', 'POSITION_IN_QUEUE']
