from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxBackupFailureDetails(BaseModel):
    Message: StrictStr | None = None
