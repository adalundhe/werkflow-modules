from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class LightsailGetInstanceAccessDetailsRequest(BaseModel):
    instanceName: StrictStr
    protocol: Literal['ssh', 'rdp'] | None = None
