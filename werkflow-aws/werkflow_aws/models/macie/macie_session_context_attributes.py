from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class MacieSessionContextAttributes(BaseModel):
    creationDate: datetime.datetime | StrictStr | None = None
    mfaAuthenticated: StrictBool | None = None
