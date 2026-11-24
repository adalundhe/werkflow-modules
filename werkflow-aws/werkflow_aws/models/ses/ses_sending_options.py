from __future__ import annotations
from pydantic import BaseModel, StrictBool


class SESSendingOptions(BaseModel):
    SendingEnabled: StrictBool | None = None
