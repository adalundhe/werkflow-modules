from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightServiceAccountCredentials(BaseModel):
    AdminAccountEmail: StrictStr
    ServiceAccountPrivateKey: StrictStr
    ClientEmail: StrictStr
