from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class AWSS3GeneratePresignedPostRequest(BaseModel):
    Bucket: StrictStr
    Key: StrictStr
    Fields: dict[str, Any] | None = None
    Conditions: list[Any] | None = None
    ExpiresIn: StrictInt = 3600
