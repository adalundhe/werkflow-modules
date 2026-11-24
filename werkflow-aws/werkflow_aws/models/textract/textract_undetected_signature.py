from __future__ import annotations
from pydantic import BaseModel, StrictInt


class TextractUndetectedSignature(BaseModel):
    Page: StrictInt | None = None
