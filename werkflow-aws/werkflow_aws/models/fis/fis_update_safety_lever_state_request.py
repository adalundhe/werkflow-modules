from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fis_update_safety_lever_state_input import FISUpdateSafetyLeverStateInput


class FISUpdateSafetyLeverStateRequest(BaseModel):
    id: StrictStr
    state: FISUpdateSafetyLeverStateInput
