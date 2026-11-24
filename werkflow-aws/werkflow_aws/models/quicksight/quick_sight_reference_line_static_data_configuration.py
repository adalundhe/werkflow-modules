from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class QuickSightReferenceLineStaticDataConfiguration(BaseModel):
    Value: StrictFloat | StrictInt | None = None
