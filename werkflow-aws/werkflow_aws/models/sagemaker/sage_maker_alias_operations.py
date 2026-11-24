from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAliasOperations(BaseModel):
    Add: list[StrictStr] | None = None
    Remove: list[StrictStr] | None = None
