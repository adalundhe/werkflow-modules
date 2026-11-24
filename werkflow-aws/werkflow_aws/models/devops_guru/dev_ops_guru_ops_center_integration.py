from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DevOpsGuruOpsCenterIntegration(BaseModel):
    OptInStatus: StrictStr | None = None
