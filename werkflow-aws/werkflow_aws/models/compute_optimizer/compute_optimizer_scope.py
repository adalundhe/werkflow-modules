from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComputeOptimizerScope(BaseModel):
    name: StrictStr | None = None
    value: StrictStr | None = None
