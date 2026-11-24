from __future__ import annotations
from typing import BinaryIO, Literal
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class CodeCommitReplaceContentEntry(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    filePath: StrictStr
    replacementType: Literal['KEEP_BASE', 'KEEP_SOURCE', 'KEEP_DESTINATION', 'USE_NEW_CONTENT']
    content: StrictBytes | BinaryIO | StrictStr | None = None
    fileMode: Literal['EXECUTABLE', 'NORMAL', 'SYMLINK'] | None = None
