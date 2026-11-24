from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class AWSS3ObjectLockLegalHold(BaseModel):
    Status: Literal['ON', 'OFF'] | None = None
