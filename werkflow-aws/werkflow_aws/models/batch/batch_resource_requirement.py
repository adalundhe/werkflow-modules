from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchResourceRequirement(BaseModel):
    value: StrictStr | None = None
    type: StrictStr | None = None
