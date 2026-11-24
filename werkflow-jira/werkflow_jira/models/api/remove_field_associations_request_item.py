from __future__ import annotations
from pydantic import BaseModel, StrictInt


class RemoveFieldAssociationsRequestItem(BaseModel):
    schemeIds: list[StrictInt] | None = None
