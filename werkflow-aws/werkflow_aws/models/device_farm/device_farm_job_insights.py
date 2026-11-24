from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .device_farm_test_report import DeviceFarmTestReport


class DeviceFarmJobInsights(BaseModel):
    status: StrictStr | None = None
    testReport: DeviceFarmTestReport | None = None
