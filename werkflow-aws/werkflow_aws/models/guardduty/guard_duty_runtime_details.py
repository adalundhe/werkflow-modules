from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_process_details import GuardDutyProcessDetails
from .guard_duty_runtime_context import GuardDutyRuntimeContext


class GuardDutyRuntimeDetails(BaseModel):
    Process: GuardDutyProcessDetails | None = None
    Context: GuardDutyRuntimeContext | None = None
