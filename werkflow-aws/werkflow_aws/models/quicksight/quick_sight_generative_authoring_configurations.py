from __future__ import annotations
from pydantic import BaseModel, StrictBool


class QuickSightGenerativeAuthoringConfigurations(BaseModel):
    Enabled: StrictBool
