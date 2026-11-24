from __future__ import annotations
from pydantic import BaseModel, StrictInt


class AWSS3NoncurrentVersionExpirationInput(BaseModel):
    NoncurrentDays: StrictInt | None = None
    NewerNoncurrentVersions: StrictInt | None = None
