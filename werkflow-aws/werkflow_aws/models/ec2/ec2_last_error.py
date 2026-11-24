from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2LastError(BaseModel):
    Message: StrictStr | None = None
    Code: StrictStr | None = None
