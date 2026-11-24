from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISExperimentReportConfigurationCloudWatchDashboard(BaseModel):
    dashboardIdentifier: StrictStr | None = None
