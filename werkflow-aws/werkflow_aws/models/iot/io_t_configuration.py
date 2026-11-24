from __future__ import annotations
from pydantic import BaseModel, StrictBool


class IoTConfiguration(BaseModel):
    Enabled: StrictBool | None = None
