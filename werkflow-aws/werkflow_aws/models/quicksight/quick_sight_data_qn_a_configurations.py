from __future__ import annotations
from pydantic import BaseModel, StrictBool


class QuickSightDataQnAConfigurations(BaseModel):
    Enabled: StrictBool
