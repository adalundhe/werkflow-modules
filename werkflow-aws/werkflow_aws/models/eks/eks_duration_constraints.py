from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSDurationConstraints(BaseModel):
    min: StrictStr | None = None
    max: StrictStr | None = None
