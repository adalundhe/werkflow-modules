from __future__ import annotations
from pydantic import BaseModel, StrictBool


class QuickSightDashboardCustomizationSummaryConfigurations(BaseModel):
    Enabled: StrictBool
