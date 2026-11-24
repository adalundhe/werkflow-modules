from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamDeleteThemeForStackRequest(BaseModel):
    StackName: StrictStr
