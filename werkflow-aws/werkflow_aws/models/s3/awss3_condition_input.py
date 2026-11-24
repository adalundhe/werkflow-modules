from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3ConditionInput(BaseModel):
    HttpErrorCodeReturnedEquals: StrictStr | None = None
    KeyPrefixEquals: StrictStr | None = None
