from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AWSS3Tiering(BaseModel):
    Days: StrictInt | None = None
    AccessTier: StrictStr | None = None
