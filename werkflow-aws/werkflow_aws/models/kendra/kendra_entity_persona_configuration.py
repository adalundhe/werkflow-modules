from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class KendraEntityPersonaConfiguration(BaseModel):
    EntityId: StrictStr
    Persona: Literal['OWNER', 'VIEWER']
