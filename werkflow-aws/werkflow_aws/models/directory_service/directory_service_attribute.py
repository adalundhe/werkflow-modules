from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceAttribute(BaseModel):
    Name: StrictStr | None = None
    Value: StrictStr | None = None
