from __future__ import annotations
from pydantic import BaseModel, StrictBool


class QuickSightBookmarksConfigurations(BaseModel):
    Enabled: StrictBool
