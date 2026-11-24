from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fis_safety_lever_state import FISSafetyLeverState


class FISSafetyLever(BaseModel):
    id: StrictStr | None = None
    arn: StrictStr | None = None
    state: FISSafetyLeverState | None = None
