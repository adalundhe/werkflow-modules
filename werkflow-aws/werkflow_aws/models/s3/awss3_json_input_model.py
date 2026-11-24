from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class AWSS3JSONInputModel(BaseModel):
    Type: Literal['DOCUMENT', 'LINES'] | None = None
