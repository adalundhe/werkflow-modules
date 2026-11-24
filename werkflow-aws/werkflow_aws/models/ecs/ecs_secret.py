from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSSecret(BaseModel):
    name: StrictStr | None = None
    valueFrom: StrictStr | None = None
