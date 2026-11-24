from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class DeviceFarmTestReportMetrics(BaseModel):
    testsTotal: StrictInt | None = None
    testsPassed: StrictInt | None = None
    testsFailed: StrictInt | None = None
    testsSkipped: StrictInt | None = None
    testsErrored: StrictInt | None = None
    testsOther: StrictInt | None = None
    testsPassedPercentage: StrictFloat | StrictInt | None = None
    totalTestExecutionDurationSeconds: StrictFloat | StrictInt | None = None
    medianTestExecutionDurationSeconds: StrictFloat | StrictInt | None = None
