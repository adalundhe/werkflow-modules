from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSAccessScope(BaseModel):
    type: StrictStr | None = None
    namespaces: list[StrictStr] | None = None
