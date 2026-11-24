from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamDescribeThemeForStackRequest(BaseModel):
    StackName: StrictStr
