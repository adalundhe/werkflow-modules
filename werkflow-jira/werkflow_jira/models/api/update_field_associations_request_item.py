from __future__ import annotations
from pydantic import BaseModel, StrictInt


class UpdateFieldAssociationsRequestItem(BaseModel):
    restrictedToWorkTypes: list[StrictInt] | None = None
    schemeIds: list[StrictInt] | None = None
