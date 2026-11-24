from __future__ import annotations
from pydantic import BaseModel, StrictBool


class MSKTableCreation(BaseModel):
    EnableTableCreation: StrictBool | None = None
