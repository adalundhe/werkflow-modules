from __future__ import annotations
from pydantic import BaseModel, StrictStr


class JqlFunctionPrecomputationUpdateBean(BaseModel):
    error: StrictStr | None = None
    id: StrictStr | None = None
    value: StrictStr | None = None
