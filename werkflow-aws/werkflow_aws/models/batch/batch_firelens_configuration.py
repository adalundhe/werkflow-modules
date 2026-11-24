from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchFirelensConfiguration(BaseModel):
    type: StrictStr | None = None
    options: dict[StrictStr, StrictStr] | None = None
