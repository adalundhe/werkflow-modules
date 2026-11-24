from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISExperimentTemplateReportConfigurationCloudWatchDashboard(BaseModel):
    dashboardIdentifier: StrictStr | None = None
