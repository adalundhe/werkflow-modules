from __future__ import annotations
from pydantic import BaseModel, StrictStr


class JqlFunctionPrecomputationUpdateResponse(BaseModel):
    notFoundPrecomputationIDs: list[StrictStr] | None = None
