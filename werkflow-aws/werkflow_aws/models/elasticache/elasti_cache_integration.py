from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheIntegration(BaseModel):
    IntegrationType: StrictStr | None = None
    Status: StrictStr | None = None
