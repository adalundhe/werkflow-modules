from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class EFSPutAccountPreferencesRequest(BaseModel):
    ResourceIdType: Literal['LONG_ID', 'SHORT_ID']
