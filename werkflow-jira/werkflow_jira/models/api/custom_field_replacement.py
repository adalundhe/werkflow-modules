from __future__ import annotations
from pydantic import BaseModel, StrictInt


class CustomFieldReplacement(BaseModel):
    customFieldId: StrictInt | None = None
    moveTo: StrictInt | None = None
