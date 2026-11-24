from __future__ import annotations
from pydantic import BaseModel, StrictBool


class CodeCommitIsBinaryFile(BaseModel):
    source: StrictBool | None = None
    destination: StrictBool | None = None
    base: StrictBool | None = None
