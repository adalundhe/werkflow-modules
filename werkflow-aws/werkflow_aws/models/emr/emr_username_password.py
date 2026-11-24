from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRUsernamePassword(BaseModel):
    Username: StrictStr | None = None
    Password: StrictStr | None = None
