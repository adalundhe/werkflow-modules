from __future__ import annotations
from pydantic import BaseModel, StrictBool


class QuickSightRecentSnapshotsConfigurations(BaseModel):
    Enabled: StrictBool
