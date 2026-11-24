from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class ConnectRulesConfiguration(BaseModel):
    Behavior: Literal['Enable', 'Disable'] | None = None
