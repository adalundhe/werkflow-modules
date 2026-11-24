from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxDataRepositoryFailureDetails(BaseModel):
    Message: StrictStr | None = None
