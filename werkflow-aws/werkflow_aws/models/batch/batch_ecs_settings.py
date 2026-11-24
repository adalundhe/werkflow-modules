from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchEcsSettings(BaseModel):
    containerInsights: StrictStr | None = None
