from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AWSS3RecordExpiration(BaseModel):
    Expiration: StrictStr | None = None
    Days: StrictInt | None = None
