from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxAdministrativeActionFailureDetails(BaseModel):
    Message: StrictStr | None = None
