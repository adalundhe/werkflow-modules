from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ACMFailureDetails(BaseModel):
    Reason: StrictStr | None = None
    Message: StrictStr | None = None
