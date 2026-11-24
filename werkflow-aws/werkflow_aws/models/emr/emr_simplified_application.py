from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRSimplifiedApplication(BaseModel):
    Name: StrictStr | None = None
    Version: StrictStr | None = None
