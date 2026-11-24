from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .device_farm_problem import DeviceFarmProblem


class DeviceFarmUniqueProblem(BaseModel):
    message: StrictStr | None = None
    problems: list[DeviceFarmProblem] | None = None
