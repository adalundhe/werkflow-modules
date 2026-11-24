from __future__ import annotations
from pydantic import BaseModel, StrictStr


class JqlFunctionPrecomputationUpdateErrorResponse(BaseModel):
    errorMessages: list[StrictStr] | None = None
    notFoundPrecomputationIDs: list[StrictStr] | None = None
