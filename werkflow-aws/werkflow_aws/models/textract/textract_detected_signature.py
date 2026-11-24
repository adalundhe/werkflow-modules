from __future__ import annotations
from pydantic import BaseModel, StrictInt


class TextractDetectedSignature(BaseModel):
    Page: StrictInt | None = None
