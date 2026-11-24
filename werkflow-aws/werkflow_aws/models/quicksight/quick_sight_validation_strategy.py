from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class QuickSightValidationStrategy(BaseModel):
    Mode: Literal['STRICT', 'LENIENT']
