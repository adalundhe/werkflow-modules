from __future__ import annotations
from pydantic import BaseModel, StrictStr


class JqlFunctionPrecomputationGetByIdRequest(BaseModel):
    precomputationIDs: list[StrictStr] | None = None
