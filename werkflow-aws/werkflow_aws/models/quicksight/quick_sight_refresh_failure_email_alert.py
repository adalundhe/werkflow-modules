from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightRefreshFailureEmailAlert(BaseModel):
    AlertStatus: StrictStr | None = None
