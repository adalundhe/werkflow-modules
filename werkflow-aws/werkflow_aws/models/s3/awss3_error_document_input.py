from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3ErrorDocumentInput(BaseModel):
    Key: StrictStr
