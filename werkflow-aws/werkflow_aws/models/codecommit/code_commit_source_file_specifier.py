from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CodeCommitSourceFileSpecifier(BaseModel):
    filePath: StrictStr
    isMove: StrictBool | None = None
