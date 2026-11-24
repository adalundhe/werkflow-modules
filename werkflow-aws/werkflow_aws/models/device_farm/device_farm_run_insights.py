from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .device_farm_job_report import DeviceFarmJobReport


class DeviceFarmRunInsights(BaseModel):
    status: StrictStr | None = None
    jobReport: DeviceFarmJobReport | None = None
