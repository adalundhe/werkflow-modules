from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchEksAccessEntry(BaseModel):
    desiredState: StrictStr | None = None
    status: StrictStr | None = None
