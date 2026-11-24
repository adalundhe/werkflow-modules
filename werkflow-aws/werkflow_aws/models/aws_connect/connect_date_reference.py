from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDateReference(BaseModel):
    Name: StrictStr | None = None
    Value: StrictStr | None = None
