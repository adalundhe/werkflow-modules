from __future__ import annotations
from typing import Any, Literal
from pydantic import BaseModel, StrictInt, StrictStr


class AWSS3GeneratePresignedURLRequest(BaseModel):
    ClientMethod: StrictStr
    Params: dict[str, Any] | None = None
    ExpiresIn: StrictInt = 3600
    HttpMethod: Literal['GET', 'PUT', 'POST', 'DELETE', 'HEAD'] | None = None
