from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessTextInputEvent(BaseModel):
    userMessage: StrictStr
