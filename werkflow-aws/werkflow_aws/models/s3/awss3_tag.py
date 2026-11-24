from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3Tag(BaseModel):
    Key: StrictStr
    Value: StrictStr
