from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class HealthCheckResult(BaseModel):
    description: StrictStr | None = None
    name: StrictStr | None = None
    passed: StrictBool | None = None
