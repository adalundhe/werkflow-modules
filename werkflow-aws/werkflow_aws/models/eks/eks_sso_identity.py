from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSSsoIdentity(BaseModel):
    id: StrictStr | None = None
    type: StrictStr | None = None
