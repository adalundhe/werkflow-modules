from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .device_farm_test_report_metrics import DeviceFarmTestReportMetrics


class DeviceFarmTestReport(BaseModel):
    message: StrictStr | None = None
    metrics: DeviceFarmTestReportMetrics | None = None
    testDetailsUrl: StrictStr | None = None
