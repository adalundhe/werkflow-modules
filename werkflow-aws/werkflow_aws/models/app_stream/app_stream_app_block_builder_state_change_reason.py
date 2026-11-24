from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamAppBlockBuilderStateChangeReason(BaseModel):
    Code: StrictStr | None = None
    Message: StrictStr | None = None
