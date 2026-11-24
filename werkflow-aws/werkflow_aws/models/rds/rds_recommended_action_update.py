from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSRecommendedActionUpdate(BaseModel):
    ActionId: StrictStr
    Status: StrictStr
