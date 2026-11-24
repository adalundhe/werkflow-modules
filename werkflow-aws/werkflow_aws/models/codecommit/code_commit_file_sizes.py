from __future__ import annotations
from pydantic import BaseModel, StrictInt


class CodeCommitFileSizes(BaseModel):
    source: StrictInt | None = None
    destination: StrictInt | None = None
    base: StrictInt | None = None
