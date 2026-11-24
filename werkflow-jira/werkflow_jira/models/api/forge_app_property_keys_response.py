from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ForgeAppPropertyKeysResponse(BaseModel):
    keys: list[StrictStr] | None = None
