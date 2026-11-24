from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FirehoseFailureDescription(BaseModel):
    Type: StrictStr | None = None
    Details: StrictStr | None = None
