from __future__ import annotations
from pydantic import BaseModel, StrictBool


class QuickSightExecutiveSummaryConfigurations(BaseModel):
    Enabled: StrictBool
