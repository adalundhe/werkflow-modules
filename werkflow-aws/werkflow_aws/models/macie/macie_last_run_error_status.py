from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieLastRunErrorStatus(BaseModel):
    code: StrictStr | None = None
