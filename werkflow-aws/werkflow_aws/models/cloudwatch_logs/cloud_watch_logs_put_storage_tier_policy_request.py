from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class CloudWatchLogsPutStorageTierPolicyRequest(BaseModel):
    storageTier: Literal['STANDARD', 'INTELLIGENT_TIERING']
