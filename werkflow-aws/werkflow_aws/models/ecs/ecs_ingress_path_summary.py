from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSIngressPathSummary(BaseModel):
    accessType: StrictStr | None = None
    endpoint: StrictStr | None = None
