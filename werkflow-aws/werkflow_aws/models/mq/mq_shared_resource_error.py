from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MQSharedResourceError(BaseModel):
    Code: StrictStr | None = None
    Message: StrictStr | None = None
