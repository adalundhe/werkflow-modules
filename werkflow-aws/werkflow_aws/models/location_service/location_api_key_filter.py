from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class LocationApiKeyFilter(BaseModel):
    KeyStatus: Literal['Active', 'Expired'] | None = None
