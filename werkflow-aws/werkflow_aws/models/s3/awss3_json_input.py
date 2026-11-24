from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class AWSS3JSONInput(BaseModel):
    Type: Literal['DOCUMENT', 'LINES'] | None = None
