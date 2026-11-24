from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchHost(BaseModel):
    sourcePath: StrictStr | None = None
