from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxDataRepositoryTaskFailureDetails(BaseModel):
    Message: StrictStr | None = None
