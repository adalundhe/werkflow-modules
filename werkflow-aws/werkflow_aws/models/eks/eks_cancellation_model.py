from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSCancellationModel(BaseModel):
    status: StrictStr | None = None
    reason: StrictStr | None = None
