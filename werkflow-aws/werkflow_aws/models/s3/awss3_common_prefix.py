from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3CommonPrefix(BaseModel):
    Prefix: StrictStr | None = None
