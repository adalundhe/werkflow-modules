from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessAppliedOrchestrationConfiguration(BaseModel):
    control: StrictStr | None = None
