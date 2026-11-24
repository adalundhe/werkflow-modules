from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class AWSS3BlockedEncryptionTypes(BaseModel):
    EncryptionType: list[Literal['NONE', 'SSE-C']] | None = None
