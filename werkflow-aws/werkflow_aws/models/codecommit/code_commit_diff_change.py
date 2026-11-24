from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CodeCommitDiffChange(BaseModel):
    type: StrictStr | None = None
    beforeLineNumber: StrictInt | None = None
    afterLineNumber: StrictInt | None = None
    content: StrictStr | None = None
