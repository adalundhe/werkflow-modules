from __future__ import annotations
from pydantic import BaseModel, StrictBool


class QuickSightStatePersistenceConfigurations(BaseModel):
    Enabled: StrictBool
