from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppRunnerTraceConfiguration(BaseModel):
    Vendor: StrictStr | None = None
