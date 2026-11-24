from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class LightsailGetRelationalDatabaseMasterUserPasswordRequest(BaseModel):
    relationalDatabaseName: StrictStr
    passwordVersion: Literal['CURRENT', 'PREVIOUS', 'PENDING'] | None = None
