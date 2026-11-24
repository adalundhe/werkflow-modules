from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CodeCommitSetFileModeEntry(BaseModel):
    filePath: StrictStr
    fileMode: Literal['EXECUTABLE', 'NORMAL', 'SYMLINK']
