from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3IndexDocument(BaseModel):
    Suffix: StrictStr | None = None
