from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class AWSS3ObjectLockLegalHoldInput(BaseModel):
    Status: Literal['ON', 'OFF'] | None = None
