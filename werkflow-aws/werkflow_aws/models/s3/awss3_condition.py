from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3Condition(BaseModel):
    HttpErrorCodeReturnedEquals: StrictStr | None = None
    KeyPrefixEquals: StrictStr | None = None
