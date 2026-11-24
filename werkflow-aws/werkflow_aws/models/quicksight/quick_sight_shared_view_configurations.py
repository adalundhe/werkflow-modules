from __future__ import annotations
from pydantic import BaseModel, StrictBool


class QuickSightSharedViewConfigurations(BaseModel):
    Enabled: StrictBool
