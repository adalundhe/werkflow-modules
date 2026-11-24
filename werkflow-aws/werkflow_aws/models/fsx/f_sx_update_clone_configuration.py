from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class FSxUpdateCloneConfiguration(BaseModel):
    SplitAction: Literal['START'] | None = None
