from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .device_farm_job_report_metrics import DeviceFarmJobReportMetrics


class DeviceFarmJobReport(BaseModel):
    message: StrictStr | None = None
    metrics: DeviceFarmJobReportMetrics | None = None
    jobDetailsUrl: StrictStr | None = None
