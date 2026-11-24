from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectActionSummary(BaseModel):
    ActionType: StrictStr | None = None
