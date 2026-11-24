from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .device_farm_device import DeviceFarmDevice
from .device_farm_problem_detail import DeviceFarmProblemDetail


class DeviceFarmProblem(BaseModel):
    run: DeviceFarmProblemDetail | None = None
    job: DeviceFarmProblemDetail | None = None
    suite: DeviceFarmProblemDetail | None = None
    test: DeviceFarmProblemDetail | None = None
    device: DeviceFarmDevice | None = None
    result: StrictStr | None = None
    message: StrictStr | None = None
