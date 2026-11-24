from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectAutomaticFailConfiguration(BaseModel):
    TargetSection: StrictStr | None = None
