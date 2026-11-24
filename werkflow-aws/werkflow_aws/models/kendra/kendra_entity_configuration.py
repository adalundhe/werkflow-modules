from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class KendraEntityConfiguration(BaseModel):
    EntityId: StrictStr
    EntityType: Literal['USER', 'GROUP']
