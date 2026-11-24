from __future__ import annotations
from pydantic import BaseModel, StrictBool


class QuickSightDataStoriesConfigurations(BaseModel):
    Enabled: StrictBool
