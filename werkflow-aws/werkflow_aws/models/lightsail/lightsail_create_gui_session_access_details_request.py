from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailCreateGUISessionAccessDetailsRequest(BaseModel):
    resourceName: StrictStr
