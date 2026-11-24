from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchEksHostPath(BaseModel):
    path: StrictStr | None = None
