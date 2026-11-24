from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class QBusinessOrchestrationConfiguration(BaseModel):
    control: Literal['ENABLED', 'DISABLED']
