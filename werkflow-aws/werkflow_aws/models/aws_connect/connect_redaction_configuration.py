from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectRedactionConfiguration(BaseModel):
    Behavior: Literal['Enable', 'Disable']
    Policy: Literal['None', 'RedactedOnly', 'RedactedAndOriginal']
    Entities: list[StrictStr] | None = None
    MaskMode: Literal['PII', 'EntityType'] | None = None
