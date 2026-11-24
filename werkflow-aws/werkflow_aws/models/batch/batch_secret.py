from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchSecret(BaseModel):
    name: StrictStr | None = None
    valueFrom: StrictStr | None = None
