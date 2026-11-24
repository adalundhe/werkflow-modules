from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitFolder(BaseModel):
    treeId: StrictStr | None = None
    absolutePath: StrictStr | None = None
    relativePath: StrictStr | None = None
