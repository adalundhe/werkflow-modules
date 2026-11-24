from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchEksEmptyDir(BaseModel):
    medium: StrictStr | None = None
    sizeLimit: StrictStr | None = None
