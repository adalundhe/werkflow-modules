from __future__ import annotations
from pydantic import BaseModel, StrictBool


class QuickSightSslProperties(BaseModel):
    DisableSsl: StrictBool | None = None
