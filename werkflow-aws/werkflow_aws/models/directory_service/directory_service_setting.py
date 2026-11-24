from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceSetting(BaseModel):
    Name: StrictStr
    Value: StrictStr
