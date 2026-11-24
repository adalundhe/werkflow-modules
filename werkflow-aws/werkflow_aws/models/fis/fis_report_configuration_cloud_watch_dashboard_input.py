from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISReportConfigurationCloudWatchDashboardInput(BaseModel):
    dashboardIdentifier: StrictStr | None = None
