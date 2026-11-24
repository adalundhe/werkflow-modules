from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GlueLakeFormationConfiguration(BaseModel):
    UseLakeFormationCredentials: StrictBool | None = None
    AccountId: StrictStr | None = None
