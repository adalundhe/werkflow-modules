from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3IndexDocumentInput(BaseModel):
    Suffix: StrictStr
