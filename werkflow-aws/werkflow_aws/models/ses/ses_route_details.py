from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESRouteDetails(BaseModel):
    Region: StrictStr
