from __future__ import annotations
from pydantic import BaseModel, StrictBool


class QuickSightThresholdAlertsConfigurations(BaseModel):
    Enabled: StrictBool
