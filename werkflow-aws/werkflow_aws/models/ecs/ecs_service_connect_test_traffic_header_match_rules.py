from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSServiceConnectTestTrafficHeaderMatchRules(BaseModel):
    exact: StrictStr | None = None
