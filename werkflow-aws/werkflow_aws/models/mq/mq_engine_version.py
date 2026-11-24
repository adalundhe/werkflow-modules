from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MQEngineVersion(BaseModel):
    Name: StrictStr | None = None
