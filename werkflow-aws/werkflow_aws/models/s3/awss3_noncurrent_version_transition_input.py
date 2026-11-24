from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt


class AWSS3NoncurrentVersionTransitionInput(BaseModel):
    NoncurrentDays: StrictInt | None = None
    StorageClass: Literal['GLACIER', 'STANDARD_IA', 'ONEZONE_IA', 'INTELLIGENT_TIERING', 'DEEP_ARCHIVE', 'GLACIER_IR'] | None = None
    NewerNoncurrentVersions: StrictInt | None = None
