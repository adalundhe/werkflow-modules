from __future__ import annotations
from pydantic import BaseModel, StrictBool


class MSKSchemaEvolution(BaseModel):
    EnableSchemaEvolution: StrictBool | None = None
