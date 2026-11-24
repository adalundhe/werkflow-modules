from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSEnvironmentFile(BaseModel):
    value: StrictStr | None = None
    type: StrictStr | None = None
