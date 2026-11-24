from __future__ import annotations
from pydantic import BaseModel, StrictBool


class QuickSightSchedulesConfigurations(BaseModel):
    Enabled: StrictBool
