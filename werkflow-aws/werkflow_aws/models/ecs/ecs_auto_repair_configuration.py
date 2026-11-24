from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSAutoRepairConfiguration(BaseModel):
    actionsStatus: StrictStr | None = None
