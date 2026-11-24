from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxFileCacheFailureDetails(BaseModel):
    Message: StrictStr | None = None
